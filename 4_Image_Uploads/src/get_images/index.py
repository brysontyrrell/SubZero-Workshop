import json
import os

import boto3

BUCKET_NAME = os.getenv('BUCKET_NAME')

s3_paginator = boto3.client('s3').get_paginator('list_objects_v2')


def lambda_handler(event, context):
    object_list = list()

    response = s3_paginator.paginate(Bucket=BUCKET_NAME, Prefix='waiting-room')

    for page in response:
        for item in page['Contents']:
            object_list.append(
                {
                    'filename': item['Key'],
                    'size': item['Size'],
                    'last_modified': item['LastModified'].isoformat()
                }
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
                "files": object_list
            }
        ),
        "headers": {
            "Content-Type": "application/json"
        },
    }
