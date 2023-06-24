from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
    App,    
)
from constructs import Construct

class VPC(Stack):
    s3_endpoint : ec2.GatewayVpcEndpoint
    vpc : ec2.Vpc

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC for the API Gateway
        self.vpc = ec2.Vpc(
            self,
            "ApiGatewayVpc",
            cidr="10.0.0.0/16",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                ),
                ec2.SubnetConfiguration(
                    name="private",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                ),
            ],
        )

        # Create an S3 Gateway VPC Endpoint
        self.s3_endpoint = ec2.GatewayVpcEndpoint(
            self, "S3Endpoint",
            service=ec2.GatewayVpcEndpointAwsService.S3,
            vpc=self.vpc
        )

        # Create a DynamoDB Gateway VPC Endpoint
        dynamodb_endpoint = ec2.GatewayVpcEndpoint(
            self, "DynamoDbEndpoint",
            service=ec2.GatewayVpcEndpointAwsService.DYNAMODB,
            vpc=self.vpc
        )

        # Add VPC endpoint for Lambda
        lambda_endpoint = self.vpc.add_interface_endpoint("LambdaEndpoint",
            service=ec2.InterfaceVpcEndpointAwsService.LAMBDA_
        )

        # Add VPC endpoint for API Gateway
        apigateway_endpoint = self.vpc.add_interface_endpoint("ApiGatewayEndpoint",
            service=ec2.InterfaceVpcEndpointAwsService.APIGATEWAY
        )         