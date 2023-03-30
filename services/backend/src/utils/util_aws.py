import boto3
from botocore.exceptions import NoCredentialsError
from src.env import BUCKET_NAME


def upload_to_aws(file, filename):
    s3 = boto3.client('s3')
    try:
        s3.upload_fileobj(file, BUCKET_NAME, filename)
        return f'https://{BUCKET_NAME}.s3.amazonaws.com/{filename}'
    except NoCredentialsError:
        return "FAILURE: AWS 자격 증명 에러"
