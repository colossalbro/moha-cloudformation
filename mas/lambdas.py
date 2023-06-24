from aws_cdk import (
    aws_ec2 as ec2,
    aws_lambda as lambda_,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    Duration,
    Stack,
    App,    
)
from .vpc import VPC
from .dynamodb import DynamoDB
from constructs import Construct

class LambdaFunction(Stack):
    account_lambda : _lambda.Function
    teams_lambda : _lambda.Function
    acct_summary_lambda : _lambda.Function
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc= VPC(self, "VPC")
        dynamodb=DynamoDB(self,"DynamoDB")
        
        # Create an AWS Lambda function
        self.account_lambda = _lambda.Function(
            self,
            "accountLambda",
            code=_lambda.Code.from_asset("mas/lambdas/accounts_lambda"),
            handler="lambda_function.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            vpc=vpc.vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            allow_public_subnet=True,
            security_groups=[ec2.SecurityGroup.from_security_group_id(self, "lambda_sg", vpc.vpc.vpc_default_security_group)],
            environment={
                "table_name":"gd_table_name"
             }
        )

        self.teams_lambda = _lambda.Function(
            self,
            "teamsLambda",
            code=_lambda.Code.from_asset("mas/lambdas/teams_lambda"),
            handler="lambda_function.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            vpc=vpc.vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            allow_public_subnet=True,
            security_groups=[ec2.SecurityGroup.from_security_group_id(self, "lambda_sg2", vpc.vpc.vpc_default_security_group)],
            environment={
                "table_name":"gd_table_name"
             }
        )


        self.acct_summary_lambda = _lambda.Function(
            self,
            "acctsummaryLambda",
            code=_lambda.Code.from_asset("mas/lambdas/acct_summary_lambda"),
            handler="lambda_function.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            vpc=vpc.vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            allow_public_subnet=True,
            security_groups=[ec2.SecurityGroup.from_security_group_id(self, "lambda_sg3", vpc.vpc.vpc_default_security_group)],
            environment={
                "bucket_name":"gd_metadata_bucket"
            }
        )
        # Create an EventBridge rule to match "PutItem" events in the DynamoDB table
        rule = events.Rule(
            self,
            "MyRule",
            event_pattern=events.EventPattern(
                source=["aws.dynamodb"],
                detail_type=["AWS API Call via CloudTrail"],
                detail={
                    "eventSource": ["dynamodb.amazonaws.com"],
                    "eventName": ["PutItem"],
                    "requestParameters": {
                        "tableName": [dynamodb.account_db.table_name],
                    },
                },
            )
        )         
        # Connect the rule to the Lambda function
        rule.add_target(targets.LambdaFunction(self.acct_summary_lambda))
        # grant the Lambda function permission to access the DynamoDB table
        dynamodb.account_db.grant_write_data(self.account_lambda)
        dynamodb.account_db.grant_write_data(self.teams_lambda)
        dynamodb.account_db.grant_read_data(self.acct_summary_lambda)                 