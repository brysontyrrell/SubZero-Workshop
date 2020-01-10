import json
import os

from aws_xray_sdk.core import patch
import boto3
from boto3.dynamodb.conditions import Key

patch(["boto3"])

TABLE_NAME = os.getenv('TABLE_NAME')

dynamodb = boto3.resource('dynamodb').Table(TABLE_NAME)


def lambda_handler(event, context):
    client_token_claims = event['requestContext']['authorizer']['claims']

    response = dynamodb.query(
        KeyConditionExpression=Key('pk').eq(client_token_claims['client_id'])
    )

    image_list = [
        {"filename": i['filename'], "sha256": i['sha256']}
        for i in response['Items']
    ]

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Success!",
                "path": event['path'],
                "method": event['httpMethod'],
                "token_claims": event['requestContext']['authorizer']['claims'],
                "files": image_list
            }
        ),
        "headers": {
            "Content-Type": "application/json"
        },
    }
