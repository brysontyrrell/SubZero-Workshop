import json
import mimetypes
import os

from aws_xray_sdk.core import patch
import boto3
from boto3.dynamodb.conditions import Key
from botocore.client import Config

patch(["boto3"])

TABLE_NAME = os.getenv('TABLE_NAME')

NOT_FOUND = {
    "isBase64Encoded": False,
    "statusCode": 404,
    "body": json.dumps({'message': "Not Found"}),
    "headers": {
        "Content-Type": "application/json"
    },
}

session = boto3.Session()
dynamodb = session.resource('dynamodb').Table(TABLE_NAME)


def lambda_handler(event, context):
    client_token_claims = event['requestContext']['authorizer']['claims']
    sha = event['pathParameters']['sha']
    try:
        size = event['queryStringParameters']['size']
    except:
        size = 0

    link_response = dynamodb.query(
        Select='COUNT',
        KeyConditionExpression=
        Key('pk').eq(client_token_claims['client_id']) & Key('sk').begins_with(sha)
    )

    if link_response['Count'] == 0:
        return NOT_FOUND

    image_response = dynamodb.get_item(Key={'pk': 'IMAGE', 'sk': sha})
    extension = mimetypes.guess_extension(image_response['Item']['mimetype'])
    key_path = os.path.join('images', sha, f"{size}{extension}")

    s3_client = session.client(
        's3',
        region_name=image_response['Item']['origin_region'],
        config=Config(signature_version='s3v4')
    )

    try:
        s3_client.head_object(Bucket=image_response['Item']['origin_bucket'], Key=key_path)
    except:
        return NOT_FOUND

    presigned_url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': image_response['Item']['origin_bucket'],
            'Key': key_path
        },
        ExpiresIn=60
    )

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Success!",
                "path": event['path'],
                "method": event['httpMethod'],
                "token_claims": event['requestContext']['authorizer']['claims'],
                "download_url": presigned_url
            }
        ),
        "headers": {
            "Content-Type": "application/json"
        },
    }
