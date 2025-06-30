import json
from db_handler import get_logs,get_logs_by_severity, get_logs_by_status
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # Convert to int if it's whole, else float
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
	print(event)
	param=json.loads(event["body"])["param"]
	response=""

	match param:
		case "all":
			response = get_logs()
		case "status":
			status=json.loads(event["body"])["status"]
			response = get_logs_by_status(status=status)
		case "severity":
			severity = json.loads(event["body"])["severity"]
			response = get_logs_by_severity(severity=severity)
	return {
		"statusCode":200,
		"body":json.dumps(response,cls=DecimalEncoder),
		"isBase64Encoded":False
	}
      