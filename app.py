#!/usr/bin/env python3
import os

import aws_cdk as cdk

from mas.mas_stack import MasStack
from mas.lambdas import LambdaFunction
from mas.api import API
from mas.s3 import S3
from mas.dynamodb import DynamoDB
from mas.vpc import VPC


app = cdk.App()
MasStack(app, "MasStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account='109661032234', region='us-east-1'),
              

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )
# API(MasStack, "API",env=cdk.Environment(account='109661032234', region='us-east-1'),)
# S3(MasStack, "S3",env=cdk.Environment(account='109661032234', region='us-east-1'),)
# VPC(MasStack, "VPC",env=cdk.Environment(account='109661032234', region='us-east-1'),)
# DynamoDB(MasStack, "DynamoDB",env=cdk.Environment(account='109661032234', region='us-east-1'),)
# LambdaFunction(MasStack, "LambdaFunction",env=cdk.Environment(account='109661032234', region='us-east-1'),)  
app.synth()
