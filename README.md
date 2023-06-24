# Title: Cloudformer APIs for M & A Accounts and Teams metadata

# Objective:

1. The hosting of a limited set of GET API methods to return metadata for M&A accounts and teams.

2. A Metadata Definition Tool that allows the population of metadata for M&A accounts and teams.

3. A means storing metadata for these accounts.  It is assumed that the metadata will be constructed manually leveraging a Metadata Definition Tool


# Pre-requisites:

1. Ensure that the AWS account has the necessary permissions to perform the required actions.

2. Ensure that the DynamoDB table is configured with the appropriate schema.

3. Ensure that the metadata store bucket has the necessary access policies to allow non-API accounts to make requests.

# Steps:

## Configure the external bucket to transfer data to DynamoDB:
a. Create a new S3 bucket in the same account as the DynamoDB table.

b. Configure the bucket to trigger an AWS Lambda function when a new object is added to the bucket.

c. Configure the Lambda function to extract the data and write it to the DynamoDB table.

## Trigger the acct summary lambda to extract and store data in metadata store bucket:
a. Create a new AWS Lambda function to extract and store the data in a metadata store bucket.

b. Configure the Lambda function to trigger when a new item is added to the DynamoDB table.

c. Ensure that the Lambda function has proper access policies to access the DynamoDB table and the metadata store bucket.

## Connect the teams lambda and accounts lambda to the DynamoDB:
a. Create two new AWS Lambda functions, one for the teams lambda and one for the accounts lambda.

b. Configure the Lambda functions to retrieve data from the DynamoDB table.

c. Ensure that the Lambda functions have the appropriate access policies to access the DynamoDB table.

## Create a private API to retrieve data from the DynamoDB table:
a. Create a new API Gateway endpoint that can be used to retrieve data from the DynamoDB table.

b. Connect the endpoint to the teams lambda and accounts lambda functions to retrieve data from the DynamoDB table.

c. Ensure that the private API Gateway endpoint has the appropriate access policies to allow PCP and other integrators  to make API requests.

## Test the setup:
a. Add new data to the external bucket and ensure that it is transferred to the DynamoDB table and the metadata store bucket.

b. Use the API Gateway endpoint to retrieve data from the DynamoDB table and ensure that the teams lambda and accounts lambda functions retrieve the data correctly.

## Conclusion:
This runbook should help you successfully set up the transfer of data from an external bucket to DynamoDB, trigger the acct summary lambda to extract and store data in a metadata store bucket, and connect two other lambdas to the DynamoDB for API get requests.
