import boto3
import json
import logging
import os

logger = logging.getLogger()
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get data from the event
    data = event['data']
    if os.environ.get("bucket_name ") is not None:
        bucket_name = os.environ.get("bucket_name ")
    else:
        error_message = "Missing environment variable bucket_name "
        logger.error(error_message)
        raise Exception(error_message)     

    # Upload data to S3 bucket
    key = 'data.json'
    s3_client.put_object(Body=data, Bucket=bucket_name, Key=key)
