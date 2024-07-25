import os

import boto3
from dotenv import load_dotenv

load_dotenv()


def create_table():
    local_db = None
    if os.environ.get("LOCAL_DB"):
        local_db = os.environ.get("LOCAL_DB")

    dynamodb = boto3.resource(
        "dynamodb",
        endpoint_url=local_db
    )

    table = dynamodb.create_table(
        TableName="tasks",
        KeySchema=[
            {
                "AttributeName": "task_id",
                "KeyType": "HASH"
            },
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "task_id",
                "AttributeType": "S"
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print("Table status:", table.table_status)


if __name__ == "__main__":
    create_table()
