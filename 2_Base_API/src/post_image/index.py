import json


def lambda_handler(event, context):
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Success!",
                "path": event['path'],
                "method": event['httpMethod']
            }
        ),
        "headers": {
            "Content-Type": "application/json"
        },
    }
