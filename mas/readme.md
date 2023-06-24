Project Summary and Vision

This document defines the requirements and high-level design for FrankenCloudformer - a limited set of Cloudformer APIs that front accounts that are hosted in the M&A Organization.   The accounts in M&A were not created by Cloudformer and therefore are not Trusted Landing Zones (TLZ) and do not conform to the account structures common to TLZ accounts.

The MnA Cloudformer Project is intended to provide a limited set of APIs that provide minimal required meta-data for the accounts that reside in the M&A organization so that global account such as Elastic Cloud, Cirrus Scan, Global Tech Registry and Public Cloud Portal can retrieve account information for accounts residing in the M&A Organization.   M&A accounts do go through an uplift process for closer alignment with KB accounts for compliance, security and observability.   Because these accounts do not follow the TLZ patterns it is anticipated that only a limited set of functionality will be supplied by the FrankenCloudformer APIs that will support this organization.


In order to accomplish this project the following will need to be addressed:

    The hosting of a limited set of GET API methods to return metadata for M&A accounts and teams.

    A Metadata Definition Tool that allows the population of metadata for M&A accounts and teams.

    A means storing metadata for these accounts.  It is assumed that the metadata will be constructed manually leveraging a Metadata Definition Tool

Use Cases

The following use cases will be supported by this project:

    As DevOps ISBAT leverage a tool that will allow me to populate the metadata for a newly uplifted M&A account.

    As GTR ISBAT retrieve limited account information for each account in MnA.

    As Cirrus Scan ISBAT retrieve limited account information for each account in MnA.

    As Elastic Cloud ISBAT retrieve limited account information for each account in MnA.

    As Portal ISBAT retrieve limited account information for each account in MnA.

    As an M&A Account Portal User ISBAT display account information for my account but I will not be able to edit account information.

    As a Infra Uplift Engineer ISBAT update the metadata for an uplifted M&A account so that other service can see and use this metadata.

Additional Requirements 

The following requirements are in addition to the above use cases:

    M&A accounts will have an environment = mna  (not prod, ote, dev, etc)

    The FrankenCloudformer APIs should run in the C3PO organization and have access to the metadata store for M&A accounts.

    FrankenCloudformer APIs should be built on the model consistent with Cloudformer 3.0 APIs for accounts and teams

    FrankenCloudformer APIs should support the following API methods:

        GET accounts

        GET accounts/id

        GET teams

        GET teams/id

    All API methods must return in < 2 seconds and optimally < 200 ms. 

    API Methods must return HTTP error codes consistent with Cloudformer API

    Based on conversations with Portal and dependent global account teams the following data should be supported when retrieving accounts

    {
        "teamName": "<name>",
        "accountId": "111111111111",
        "accountName": "GD-AWS-Global-Audit-Test-<env>",
        "environment": "<env>",
        "onCallGroup": "DEV-AppSecurity",
        "regionNames": [
            "us-west-2"

                ],

    The /3.0/accounts api should support the following metadata:

        Fields highlighted in RED are candidate for meta-data for M&A Accounts

{
  "data": [
    {
      "alias": "string",
      "accountDL": {

“emailAddress“: string,

“members”: [“string”],

“owner”: string

      },

      "adGoups {  

“members”: [“string”],

“name”: string

      },

      “alias”: string,
      "architectureType": "None",
      "awsAccountId": 0,
      "awsOrganization": "string",
      "budgetId": "string",

      “canModify”: bool,
      "createDate": "string",

      "enableLegacyServiceAccounts": false,
      "environment": "mna",
      "envMode": "prod",
      "esspDestination": "string",
      "id": "string",
      "isGlobal": false,
      "isGoldenAmi": false,
      "isMLAccount": false,
      "isPii": false,
      "lastModifiedDate": "string",
      "name": "string",
      "onCallGroup": "string",

      "operationsDL": {

“emailAddress“: string,

“members”: [“string”],

“owner”: string

      },
      "orgType": "mna",
      "piaId": "string",
      "regions": [
        {
          "hasBaselineStack": true,
          "hasLoggingStack": true,
          "hasServiceCatalogStack": true,
          "name": "string",
          "vpcs": [
            {
              "azCount": 0,
              "configOption": "string",
              "hasDirectConnect": true,
              "hasSingleNatGateway": true,
              "id": "string",
              "isIpv6Enabled": false,
              "networkAssignments": [
                {
                  "id": 0,
                  "cidr": "string",
                  "subnetGroupId": “string”
                }
              ],
              "subnetGroups": [
                {

                  “id”: “string”,
                  "isBoltOn": true,

                  "isRoutable": true,
                  "subnets": [
                    {
                      "availabilityZone": "string",
                      "cidr": "string",
                      "rootCidr": "string"
                     }
                   ],
                   "type": "string"
                }
              ],
              "suffix": "string"
            }
          ]
        }
     ],     

      "securityDL": {

“emailAddress“: string,

“members”: [“string”],

“owner”: string

      },     
      "serviceAccountUser": {
        "secretKey”: "string",
        "secretRegion": "string",
        "userName": "string"
      },

      “slack”: {

 "channel": "string",
  "webHook": "string"

      },     
      "state": "metadata only",
      "status": "metadata only",
      "team": {

“id”: “string”,

"name": "string"

       },
      
      "teamNameEnvironment": "string",
      "type": "string"
    }
  ]
}

NOTE:  we’ll probably want to defer to the portal team on whether the “regions” list is necessary or just the “regionNames” list. depends on how they plan to represent things most likely.

 

    The /3.0/teams api should support the following metadata:

        Fields highlighted in RED are candidate for meta-data for M&A Accounts

            {
              "data": [
                {
                  "awsOrganization": "string",
                  "billingDL": "string",
                  "billingDLMembers": "string",
                  "billingDLOwner": "string",
                  "budgetId": "string",
                  "createDate": "string",
                  "esspDeploys": [
                    {
                      "enabled": true,
                      "kibanaAdminADGroup": "string",
                      "kibanaReadOnlyADGroup": "string",
                      "kibanaUrl": "string",
                      "resources": [
                        {
                          "memory": 0,
                          "node_type": "string",
                          "zone_count": 0
                        }
                      ],
                      "type": "string",
                      "version": "string",
                      "graviton": true
                    }
                  ],
                  "esspRegion": "string",
                  "lastModifiedDate": "string",
                  "legalName": "USA",
                  "teamDL": "string",
                  "teamName": "string",
                  "vpcVersion": "1.0"
                }
              ]
            }

    The metadata tool must align with the following:

        Must be able to store the required data for accounts and teams

        Must able to set values to default if there are no known values for the field 

        Must be able to allow the tool user to update a single field

        Must be integrated with Okta for authentication

        Must ensure that only specific individuals have the privileges to change metadata

        M&A metadata should reside in the AccountAutomation-Prod account in C3PO

        Suggest that a GitHub commit adds the metadata to the metadata store.