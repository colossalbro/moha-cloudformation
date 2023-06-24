from aws_cdk import (
    aws_iam as _iam,
    aws_s3 as s3,
    RemovalPolicy,
    Stack,
    App,    
)
from .lambdas import LambdaFunction
from .vpc import VPC
from constructs import Construct

class S3(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambda_=LambdaFunction(self,"LambdaFunction")
        vpc= VPC(self, "VPC")        
        # creating metadata bucket
        metadata_bucket = s3.Bucket(
            self,
            "gd_metadata_Bucket",
            bucket_name="gd-metadata-bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
        )

        # Configure the S3 bucket policy to allow access from the VPC endpoint
        metadata_bucket.add_to_resource_policy(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                principals=[_iam.AnyPrincipal()],
                actions=["s3:*"],
                resources=[metadata_bucket.arn_for_objects("*")],
                conditions={
                    "StringEquals": {
                        "aws:SourceVpce": vpc.s3_endpoint.vpc_endpoint_id
                    }
                },
            )
        )

        # Grant read access to the Lambda function from the S3 bucket
        metadata_bucket.grant_write(lambda_.acct_summary_lambda)   