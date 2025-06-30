import boto3
import os
import uuid
from datetime import datetime, date
from decimal import Decimal

TABLE_NAME = os.environ["INCIDENT_TABLE"]

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def store_incident(message):
    current_date =  date.today().strftime("%m-%d-%Y")
    current_timestamp=int(datetime.now().timestamp())
    severity = message["severity"]
    summary = message["summary"]
    suggestions = message["suggestions"]
    log_group = message["log_group"]
    log_message=message["log_message"]

    table.put_item(
        Item={
                "date":current_date,
                "eventId": str(uuid.uuid4()),
                "timestamp":current_timestamp,
                "severity":severity,
                "summary":summary,
                "suggestions":suggestions,
                "status":"OPEN",
                "source": log_group,
                "log_text": log_message
            }
        )
