import json
import boto3
from botocore.exceptions import ClientError
bedrock = boto3.client('bedrock-runtime', region_name='ap-south-1')  # or your region

MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

def build_prompt(log_text):
    return {
        "messages": [
            {
                "role": "user",
                "content":  f"""You are an intelligent incident response assistant.

                                Given the following application logs, analyze and return the output strictly in the following JSON format:

                                {{
                                "severity": "Critical/High/Medium/Low",
                                "summary": "<Concise two-line summary of the issue>",
                                "suggestions": "<One-line suggestion or possible fix>"
                                }}

                                Only respond with the JSON. Do not include any explanation or extra text.

                                Here are the logs:

                                {log_text}"""
            }
        ],
        "max_tokens": 500,
        "anthropic_version": "bedrock-2023-05-31",
    }

def analyse_log(log_message):
    prompt = build_prompt(log_message)
    
    print("Invoking bedrock...")
    try:
        # Invoke the model with the request.
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(prompt),
            contentType="application/json",
            accept="application/json"
        )

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{MODEL_ID}'. Reason: {e}")
        exit(1)

    model_response = json.loads(response["body"].read())
    print("model response: ", model_response)

    # Extract and print the response text.
    response_text = model_response["content"][0]['text']
    return json.loads(response_text)