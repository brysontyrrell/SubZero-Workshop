import hashlib
import json
import os
import time

from aws_xray_sdk.core import patch
import boto3

patch(["boto3"])

AWS_REGION = os.getenv('AWS_REGION')
STEP_FUNCTION_ARN = os.getenv("STEP_FUNCTION_ARN")

s3_client = boto3.client('s3')
sf_client = boto3.client("stepfunctions")


def lambda_handler(event, context):
    for record in get_s3_records(event):
        source_bucket = record["s3"]["bucket"]["name"]
        source_key = record["s3"]["object"]["key"]

        metadata = s3_client.head_object(
            Bucket=source_bucket,
            Key=source_key
        )

        filename_hash = hashlib.sha1(metadata['Metadata']['filename'].encode()).hexdigest()

        sf_client.start_execution(
            stateMachineArn=STEP_FUNCTION_ARN,
            name=f"{metadata['Metadata']['uploading-client']}-{int(time.time())}",
            input=json.dumps(
                dict(
                    {
                        'bucket': source_bucket,
                        'key': source_key,
                        'filaname_hash': filename_hash,
                        'composite': f"{metadata['Metadata']['sha256-hash']}_{filename_hash}",
                        "mimetype": metadata['ContentType'],
                        "origin-bucket": source_bucket,
                        "origin-region": AWS_REGION
                    },
                    **metadata['Metadata']
                )
            )
        )


def get_s3_records(event):
    for message in event["Records"]:
        try:
            records = json.loads(message["body"])["Records"]
        except KeyError:
            return list()

        for record in records:
            yield record
