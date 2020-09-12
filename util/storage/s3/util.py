import boto3
import logging
from botocore.exceptions import ClientError
from botocore.client import Config

from config.storage import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_ENDPOINT_URL, S3_PRESIGNED_URL_EXPIRY_TIMEOUT, S3_DEFAULT_BUCKET_NAME, S3_DEFAULT_BUCKET_REGION


def create_presigned_url_post(object_name: str) -> dict:
    """
    Generate a presigned URL S3 POST request to upload a file

    :param bucket_name: string
    :param object_name: string
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    s3_client = boto3.client(
        's3',
        endpoint_url=S3_ENDPOINT_URL,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=S3_DEFAULT_BUCKET_REGION
    )

    try:
        response = s3_client.generate_presigned_post(
            S3_DEFAULT_BUCKET_NAME,
            object_name,
            Fields=None,
            Conditions=None,
            ExpiresIn=S3_PRESIGNED_URL_EXPIRY_TIMEOUT
        )

    except ClientError as e:
        logging.error(e)
        return None

    return response
