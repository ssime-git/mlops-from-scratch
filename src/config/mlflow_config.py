import mlflow
import os
import boto3
from botocore.client import Config

def setup_mlflow():
    """
    Set up MLflow tracking URI and S3 endpoint URL.
    """
    mlflow.set_tracking_uri("http://localhost:5000")
    
    # MinIO configuration
    os.environ['MLFLOW_S3_ENDPOINT_URL'] = 'http://localhost:9002'
    os.environ['AWS_ACCESS_KEY_ID'] = 'minioadmin'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'minioadmin'

    # Create the 'mlflow' bucket if it doesn't exist
    s3_client = boto3.client('s3',
                             endpoint_url=os.environ['MLFLOW_S3_ENDPOINT_URL'],
                             aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                             aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                             config=Config(signature_version='s3v4'),
                             region_name='us-east-1')
    
    try:
        s3_client.head_bucket(Bucket='mlflow')
    except:
        s3_client.create_bucket(Bucket='mlflow')

    # Set the default artifact store
    mlflow.set_experiment("default")

    print("MLflow configuration completed successfully.")