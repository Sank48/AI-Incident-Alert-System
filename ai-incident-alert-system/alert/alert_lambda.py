import json
import gzip
import base64
from io import BytesIO
from datetime import datetime

from bedrock_handler import analyse_log
from db_handler import store_incident
from email_handler import send_email
def lambda_handler(event, context):
    # Example: Read logs from incoming CloudWatch event
    print("Event: ", event)
    logs = event['awslogs']['data']
    compressed_payload = base64.b64decode(logs)

    # Step 2: decompress gzip
    with gzip.GzipFile(fileobj=BytesIO(compressed_payload)) as f:
        decompressed_data = f.read()

    # Step 3: parse JSON
    log_data = json.loads(decompressed_data)
    print("log_data: ", log_data)
    print("Log group: ", log_data['logGroup'])

    # Now you can access log events
    for log_event in log_data['logEvents']:
        if 'ERROR' in log_event['message']:
            print(f"Message: {log_event['message']}")
            log_message= log_event['message']

    response = analyse_log(log_message=log_message)
    response["log_group"]=log_data["logGroup"]
    response["log_message"]=log_message
    store_incident(message=response)

    if response["severity"] == "Critical":
        send_email(subject=response["summary"], log_text=log_message)

    print("Incident is analysed, stored and notified successfully!")
    

