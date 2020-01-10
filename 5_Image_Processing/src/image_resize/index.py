from io import BytesIO
import mimetypes
import os

from aws_xray_sdk.core import patch
import boto3
from PIL import Image

patch(["boto3"])

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    image = load_image(event['bucket'], event['key'])

    if event['image_size'] > 0:
        image = scale(event['image_size'], image)

    extension = mimetypes.guess_extension(event['mimetype'])
    key_path = os.path.join(
        'images', event['sha256'], f"{event['image_size']}{extension}"
    )

    save_image(event['bucket'], key_path, image, event['mimetype'])

    return {'ImagePath': key_path}


def load_image(bucket, key):
    fileobj = BytesIO()
    s3_client.download_fileobj(Bucket=bucket, Key=key, Fileobj=fileobj)
    return Image.open(fileobj)


def scale(width, image):
    percentage = (float(width) / float(image.size[0]))
    new_height = int((float(image.size[1]) * float(percentage)))
    return image.resize((width, new_height), Image.ANTIALIAS)


def save_image(bucket, key, image, mimetype):
    fileobj = BytesIO()
    image.save(fileobj, format=key.split('.')[-1])
    fileobj.seek(0)
    s3_client.upload_fileobj(
        Bucket=bucket,
        Key=key,
        Fileobj=fileobj,
        ExtraArgs={'ContentType': mimetype}
    )
