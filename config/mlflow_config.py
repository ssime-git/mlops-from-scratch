# File: mlops-project/config/mlflow_config.py

import mlflow
import os

def setup_mlflow():
    """
    Set up MLflow tracking URI and S3 endpoint URL.
    """
    mlflow.set_tracking_uri("http://mlflow:5000")
    os.environ['MLFLOW_S3_ENDPOINT_URL'] = 'http://minio:9000'
    os.environ['AWS_ACCESS_KEY_ID'] = 'minioadmin'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'minioadmin'