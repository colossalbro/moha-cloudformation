import aws_cdk as core
import aws_cdk.assertions as assertions

from mas.mas_stack import MasStack

# example tests. To run these tests, uncomment this file along with the example
# resource in mas/mas_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MasStack(app, "mas")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
