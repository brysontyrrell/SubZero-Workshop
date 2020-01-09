import base64
from cgi import parse_header
import hashlib
import json
import os

import boto3
from requests_toolbelt import multipart

ACCEPTED_CONTENT_TYPE = 'multipart/form-data'
BUCKET_NAME = os.getenv('BUCKET_NAME')

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    client_token_claims = event['requestContext']['authorizer']['claims']
    content_type = event['headers'].get('Content-Type', '')

    if not content_type_check(content_type):
        return {
            "isBase64Encoded": False,
            "statusCode": 415,
            "body": json.dumps({'message': 'Unsupported Media Type'}),
            "headers": {
                "Content-Type": "application/json"
            }
        }

    raw_body = base64.b64decode(event['body'])
    multipart_data = multipart.decoder.MultipartDecoder(raw_body, content_type)
    # {'name': 'file', 'filename': 'filename.png'}
    _, multipart_headers = parse_header(
        multipart_data.parts[0].headers[b'Content-Disposition'].decode()
    )
    multipart_binary_content = multipart_data.parts[0].content
    multipart_content_type = multipart_data.parts[0].headers[b'Content-Type'].decode()

    sha_256_hash = hashlib.sha256(multipart_binary_content).hexdigest()

    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=os.path.join('waiting-room', sha_256_hash),
        Body=multipart_binary_content,
        ContentType=multipart_content_type,
        Metadata={
            "uploading-client": client_token_claims['client_id'],
            "sha256-hash": sha_256_hash,
            "filename": multipart_headers.get('filename')
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
                "token_claims": client_token_claims,
                "file": {
                    "filename": multipart_headers.get('filename'),
                    "mime-type": multipart_content_type,
                    "size": len(multipart_binary_content),
                    "sha256": sha_256_hash
                }
            }
        ),
        "headers": {
            "Content-Type": "application/json"
        },
    }


def content_type_check(value):
    if value.split(';')[0] == ACCEPTED_CONTENT_TYPE:
        return True
    return False
