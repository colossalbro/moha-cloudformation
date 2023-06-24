from aws_cdk import (
    aws_ec2 as ec2,
    aws_lambda as lambda_,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as _dynamodb,
    aws_iam as _iam,
    aws_logs as logs,
    aws_events as events,
    aws_events_targets as targets,
    Duration,
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    App,
)
from constructs import Construct
from .lambdas import LambdaFunction
from .api import API
from .s3 import S3
from .dynamodb import DynamoDB
from .vpc import VPC

class MasStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        vpc= VPC(self, "VPC")
        lambda_=LambdaFunction(self,"LambdaFunction")
        api=API(self,"API")
        s3=S3(self,"S3")
        dynamodb=DynamoDB(self,"DynamoDB")



        # # Create a VPC for the API Gateway
        # vpc = ec2.Vpc(
        #     self,
        #     "ApiGatewayVpc",
        #     cidr="10.0.0.0/16",
        #     max_azs=2,
        #     subnet_configuration=[
        #         ec2.SubnetConfiguration(
        #             name="public",
        #             subnet_type=ec2.SubnetType.PUBLIC,
        #         ),
        #         ec2.SubnetConfiguration(
        #             name="private",
        #             subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
        #         ),
        #     ],
        # )
        # api_policy = _iam.PolicyDocument(
        #     statements=[
        #         _iam.PolicyStatement(
        #             effect=_iam.Effect.ALLOW,
        #             principals=[_iam.AnyPrincipal()],
        #             actions=["execute-api:Invoke"],
        #             resources=["*"],
        #         )
        #     ],
        # )
        # # Create a Private API Gateway
        # api = apigw.RestApi(
        #     self,
        #     "MyApi",
        #     policy=api_policy,
        #     endpoint_configuration=apigw.EndpointConfiguration(
        #         types=[apigw.EndpointType.PRIVATE]
        #     ),
        # )        

        # # Create an S3 Gateway VPC Endpoint
        # s3_endpoint = ec2.GatewayVpcEndpoint(
        #     self, "S3Endpoint",
        #     service=ec2.GatewayVpcEndpointAwsService.S3,
        #     vpc=vpc
        # )

        # # Create a DynamoDB Gateway VPC Endpoint
        # dynamodb_endpoint = ec2.GatewayVpcEndpoint(
        #     self, "DynamoDbEndpoint",
        #     service=ec2.GatewayVpcEndpointAwsService.DYNAMODB,
        #     vpc=vpc
        # )

        # # Add VPC endpoint for Lambda
        # lambda_endpoint = vpc.add_interface_endpoint("LambdaEndpoint",
        #     service=ec2.InterfaceVpcEndpointAwsService.LAMBDA_
        # )

        # # Add VPC endpoint for API Gateway
        # apigateway_endpoint = vpc.add_interface_endpoint("ApiGatewayEndpoint",
        #     service=ec2.InterfaceVpcEndpointAwsService.APIGATEWAY
        # ) 

        # # Create an AWS Lambda function
        # account_lambda = _lambda.Function(
        #     self,
        #     "accountLambda",
        #     code=_lambda.Code.from_asset("mas/lambdas/accounts_lambda"),
        #     handler="lambda_function.lambda_handler",
        #     runtime=_lambda.Runtime.PYTHON_3_8,
        #     vpc=vpc,
        #     vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
        #     allow_public_subnet=True,
        #     security_groups=[ec2.SecurityGroup.from_security_group_id(self, "lambda_sg", vpc.vpc_default_security_group)],
        #     environment={
        #         "table_name":"gd_table_name"
        #      }
        # )

        # teams_lambda = _lambda.Function(
        #     self,
        #     "teamsLambda",
        #     code=_lambda.Code.from_asset("mas/lambdas/teams_lambda"),
        #     handler="lambda_function.lambda_handler",
        #     runtime=_lambda.Runtime.PYTHON_3_8,
        #     vpc=vpc,
        #     vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
        #     allow_public_subnet=True,
        #     security_groups=[ec2.SecurityGroup.from_security_group_id(self, "lambda_sg2", vpc.vpc_default_security_group)],
        #     environment={
        #         "table_name":"gd_table_name"
        #      }
        # )


        # acct_summary_lambda = _lambda.Function(
        #     self,
        #     "acctsummaryLambda",
        #     code=_lambda.Code.from_asset("mas/lambdas/acct_summary_lambda"),
        #     handler="lambda_function.lambda_handler",
        #     runtime=_lambda.Runtime.PYTHON_3_8,
        #     vpc=vpc,
        #     vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
        #     allow_public_subnet=True,
        #     security_groups=[ec2.SecurityGroup.from_security_group_id(self, "lambda_sg3", vpc.vpc_default_security_group)],
        #     environment={
        #         "bucket_name":"gd_metadata_bucket"
        #     }
        # )  
              
        # # Connect the integration to a new API Gateway resource
        # p_api_acct = api.root.add_resource("3.0").add_resource("Accts")
        # p_api_teams = api.root.add_resource("3.0v").add_resource("Teams")


        # # Create an integration between the API Gateway and the Lambda function
        # integration_acct = apigw.LambdaIntegration(
        #     handler=account_lambda
        #         )
        # integration_teams = apigw.LambdaIntegration(
        #     handler=teams_lambda
        #         )

        # p_api_acct.add_method("GET", integration_acct)
        # p_api_teams.add_method("GET", integration_teams)

        # # DynamoDB implementation
        # account_db = _dynamodb.Table(
        #     self,
        #     "AccountDB",
        #     partition_key=_dynamodb.Attribute(
        #         name="teamName", type=_dynamodb.AttributeType.STRING
        #     ),
        #     sort_key=_dynamodb.Attribute(
        #         name="accountId", type=_dynamodb.AttributeType.NUMBER
        #     ),
        #     table_name="gd_table_name",
        #     billing_mode=_dynamodb.BillingMode.PAY_PER_REQUEST,
        #     removal_policy=RemovalPolicy.DESTROY,
        #     point_in_time_recovery=True,
        # )   
        # # grant the Lambda function permission to access the DynamoDB table
        # account_db.grant_write_data(account_lambda)
        # account_db.grant_write_data(teams_lambda)
        # account_db.grant_read_data(acct_summary_lambda)

        # # adding local secondary index
        # account_db.add_local_secondary_index(
        #     index_name="accountName",
        #     sort_key=_dynamodb.Attribute(
        #         name="accountName",
        #         type=_dynamodb.AttributeType.STRING,
        #     ),
        # )

        # account_db.add_local_secondary_index(
        #     index_name="environment",
        #     sort_key=_dynamodb.Attribute(
        #         name="environment", type=_dynamodb.AttributeType.STRING
        #     ),
        # )

        # account_db.add_local_secondary_index(
        #     index_name="onCallGroup",
        #     sort_key=_dynamodb.Attribute(
        #         name="onCallGroup",
        #         type=_dynamodb.AttributeType.STRING,
        #     ),
        # )

        # account_db.add_local_secondary_index(
        #     index_name="regionNames",
        #     sort_key=_dynamodb.Attribute(
        #         name="regionNames", type=_dynamodb.AttributeType.STRING
        #     ),
        # )
        # account_db.add_local_secondary_index(
        #     index_name="data",
        #     sort_key=_dynamodb.Attribute(
        #         name="data", type=_dynamodb.AttributeType.STRING
        #     ),
        # )
        # # # Hold for 5 years; backup daily
        # # plan = _backup.BackupPlan.daily_weekly_monthly5_year_retention(
        # #     self, config["backup"]["accounts_ddb_backup_policy_name"]
        # # )

        # # plan.add_rule(
        # #     _backup.BackupPlanRule(
        # #         enable_continuous_backup=True, delete_after=Duration.days(35)
        # #     )
        # # )

        # # # Backup the Account Table
        # # plan.add_selection(
        # #     "Selection",
        # #     resources=[_backup.BackupResource.from_dynamo_db_table(account_db)],
        # # )

        # # Create an EventBridge rule to match "PutItem" events in the DynamoDB table
        # rule = events.Rule(
        #     self,
        #     "MyRule",
        #     event_pattern=events.EventPattern(
        #         source=["aws.dynamodb"],
        #         detail_type=["AWS API Call via CloudTrail"],
        #         detail={
        #             "eventSource": ["dynamodb.amazonaws.com"],
        #             "eventName": ["PutItem"],
        #             "requestParameters": {
        #                 "tableName": [account_db.table_name],
        #             },
        #         },
        #     )
        # )

        # # Connect the rule to the Lambda function
        # rule.add_target(targets.LambdaFunction(acct_summary_lambda))
        # # creating metadata bucket
        # metadata_bucket = s3.Bucket(
        #     self,
        #     "gd_metadata_Bucket",
        #     bucket_name="gd-metadata-bucket",
        #     block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        #     removal_policy=RemovalPolicy.DESTROY,
        # )

        # # Configure the S3 bucket policy to allow access from the VPC endpoint
        # metadata_bucket.add_to_resource_policy(
        #     _iam.PolicyStatement(
        #         effect=_iam.Effect.ALLOW,
        #         principals=[_iam.AnyPrincipal()],
        #         actions=["s3:*"],
        #         resources=[metadata_bucket.arn_for_objects("*")],
        #         conditions={
        #             "StringEquals": {
        #                 "aws:SourceVpce": s3_endpoint.vpc_endpoint_id
        #             }
        #         },
        #     )
        # )

        # # Grant read access to the Lambda function from the S3 bucket
        # metadata_bucket.grant_write(acct_summary_lambda)   

