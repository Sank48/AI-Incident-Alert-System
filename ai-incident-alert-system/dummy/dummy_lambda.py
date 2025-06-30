import json

ERROR_TEMPLATES = {
    "DB_ERROR": "Error: Failed to connect to database.\n  at DB.connect (/app/db.py:45)",
    "AUTH_FAILURE": "Error: Unauthorized access attempt detected.\n  at AuthService.verify_token (/auth/service.py:78)",
    "SERVICE_DOWN": "Error: Downstream service 'UserService' is not responding (HTTP 503).\n  at Service.call (/services/user.py:122)",
    "TIMEOUT": "Error: Request to PaymentService timed out after 30s.\n  at payment.process (/app/payment.py:56)",
    "NULL_POINTER": "Traceback (most recent call last):\n  File \"main.py\", line 32, in <module>\n    print(obj.attr)\nAttributeError: 'NoneType' object has no attribute 'attr'",
    "RATE_LIMIT": "Error: Rate limit exceeded (HTTP 429) for endpoint /api/v1/messages\n  at api_gateway.request (/gateway/api.py:94)",
    "DISK_FULL": "OSError: [Errno 28] No space left on device\n  at FileWriter.write (/system/storage.py:88)",
    "MEMORY_LEAK": "Warning: Possible memory leak detected - heap usage exceeded 1.5GB\n  at profiler.track (/tools/memory.py:55)",
    "CONFIG_MISSING": "Error: Missing required configuration: DB_PASSWORD\n  at config.load (/config/settings.py:14)",
    "DEPLOY_ERROR": "Deployment failed: Docker build exited with code 137\n  at step 'Build Image' in CI/CD pipeline",
    "INTERNAL_ERROR": "Error: Internal server error occurred (500)\n  at /routes/api.py:203",
    "INVALID_INPUT": "ValueError: Invalid input: 'email' must be a valid email string\n  at validate_input (/utils/validation.py:47)"
}

def lambda_handler(event, context):
    # Simulated failure to produce ERROR logs
    # print("INFO: Dummy Lambda triggered.")
    # print("WARN: Attempting to call downstream service.")
    # raise Exception("ERROR: Simulated failure - Database connection timed out.")

    error_type=json.loads(event["body"])["type"]
    raise Exception(ERROR_TEMPLATES[error_type])
    

