import json
import boto3
import logging
import os

logger = logging.getLogger()
dynamodb = boto3.resource('dynamodb')

table_name = ''

def lambda_handler(event, context):
    metadata = event
    if os.environ.get("table_name") is not None:
        table_name = os.environ.get("table_name")
    else:
        error_message = "Missing environment variable table_name"
        logger.error(error_message)
        raise Exception(error_message)    
    table = dynamodb.Table(table_name)
    table.put_item(Item={
        'metadata': metadata
    })
    logger.info(event)
    return {
        'statusCode': 200,
        'body': json.dumps(f'Metadata added to DynamoDB table {event}')
    }