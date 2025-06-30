import boto3
import os
from datetime import date
from boto3.dynamodb.conditions import Key

db=boto3.resource("dynamodb")
table=db.Table(os.environ["INCIDENT_TABLE"])

def get_logs():
    current_date=date.today().strftime("%m-%d-%Y")
    response = table.query(
        KeyConditionExpression = Key('date').eq(current_date),
        ScanIndexForward=False,
        Limit=10
    )

    return response["Items"]

def get_logs_by_severity(severity):
    response = table.query(
        IndexName="SeverityIndex",
        KeyConditionExpression = Key('severity').eq(severity),
        ScanIndexForward=False,
        Limit=10
    )
    return response["Items"]

def get_logs_by_status(status):
    response = table.query(
        IndexName="StatusIndex",
        KeyConditionExpression = Key('status').eq(status),
        ScanIndexForward=False,
        Limit=10
    )
    return response["Items"]
