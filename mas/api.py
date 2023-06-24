from aws_cdk import (
    aws_apigateway as apigw,
    aws_iam as _iam,
    Stack,
    App,

)
from .lambdas import LambdaFunction
from constructs import Construct

class API(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambda_=LambdaFunction(self,"LambdaFunction")       
        # CREATE API POLICY 
        api_policy = _iam.PolicyDocument(
            statements=[
                _iam.PolicyStatement(
                    effect=_iam.Effect.ALLOW,
                    principals=[_iam.AnyPrincipal()],
                    actions=["execute-api:Invoke"],
                    resources=["*"],
                )
            ],
        )
        # Create a Private API Gateway
        api = apigw.RestApi(
            self,
            "MyApi",
            policy=api_policy,
            endpoint_configuration=apigw.EndpointConfiguration(
                types=[apigw.EndpointType.PRIVATE]
            ),
        ) 

        # Connect the integration to a new API Gateway resource
        p_api_acct = api.root.add_resource("3.0").add_resource("Accts")
        p_api_teams = api.root.add_resource("3.0v").add_resource("Teams")


        # Create an integration between the API Gateway and the Lambda function
        integration_acct = apigw.LambdaIntegration(
            handler=lambda_.account_lambda
                )
        integration_teams = apigw.LambdaIntegration(
            handler=lambda_.teams_lambda
                )

        p_api_acct.add_method("GET", integration_acct)
        p_api_teams.add_method("GET", integration_teams)