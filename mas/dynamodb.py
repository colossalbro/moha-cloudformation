from aws_cdk import (
    aws_dynamodb as _dynamodb,
    aws_events as events,
    aws_events_targets as targets,
    Duration,
    Stack,
    RemovalPolicy,
    App,
)
from constructs import Construct

class DynamoDB(Stack):
    account_db : _dynamodb.Table
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # DynamoDB implementation
        self.account_db = _dynamodb.Table(
            self,
            "AccountDB",
            partition_key=_dynamodb.Attribute(
                name="teamName", type=_dynamodb.AttributeType.STRING
            ),
            sort_key=_dynamodb.Attribute(
                name="accountId", type=_dynamodb.AttributeType.NUMBER
            ),
            table_name="gd_table_name",
            billing_mode=_dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
            point_in_time_recovery=True,
        )   


        # adding local secondary index
        self.account_db.add_local_secondary_index(
            index_name="accountName",
            sort_key=_dynamodb.Attribute(
                name="accountName",
                type=_dynamodb.AttributeType.STRING,
            ),
        )

        self.account_db.add_local_secondary_index(
            index_name="environment",
            sort_key=_dynamodb.Attribute(
                name="environment", type=_dynamodb.AttributeType.STRING
            ),
        )

        self.account_db.add_local_secondary_index(
            index_name="onCallGroup",
            sort_key=_dynamodb.Attribute(
                name="onCallGroup",
                type=_dynamodb.AttributeType.STRING,
            ),
        )

        self.account_db.add_local_secondary_index(
            index_name="regionNames",
            sort_key=_dynamodb.Attribute(
                name="regionNames", type=_dynamodb.AttributeType.STRING
            ),
        )
        self.account_db.add_local_secondary_index(
            index_name="data",
            sort_key=_dynamodb.Attribute(
                name="data", type=_dynamodb.AttributeType.STRING
            ),
        )
        # # Hold for 5 years; backup daily
        # plan = _backup.BackupPlan.daily_weekly_monthly5_year_retention(
        #     self, config["backup"]["accounts_ddb_backup_policy_name"]
        # )

        # plan.add_rule(
        #     _backup.BackupPlanRule(
        #         enable_continuous_backup=True, delete_after=Duration.days(35)
        #     )
        # )

        # # Backup the Account Table
        # plan.add_selection(
        #     "Selection",
        #     resources=[_backup.BackupResource.from_dynamo_db_table(self.account_db)],
        # )



