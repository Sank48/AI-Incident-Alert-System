import boto3
import os
import json

ses = boto3.client('ses', region_name="ap-south-1")
EMAIL_TO = os.environ.get("EMAIL_TO")

def send_email(subject, log_text):
    ses.send_email(
        Source=EMAIL_TO,
        Destination={'ToAddresses': [EMAIL_TO]},
        Message={
            'Subject': {'Data': f"[CRITICAL] {subject}"},
            'Body': {'Text': {'Data': f"Critical incident detected:\n\n{log_text}"}}
        }
    )
