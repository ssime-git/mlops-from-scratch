# File: src/data_ingestion/ingestion.py

import pandas as pd
from sklearn.datasets import load_iris
import mlflow
import os
from config.mlflow_config import setup_mlflow
from onfig.logging_config import setup_logging


logger = setup_logging()

def ingest_data():
    """
    Ingest the Iris dataset, save it as a CSV, and log it with MLflow.
    """
    logger.info("Starting data ingestion process")

    # Load Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Save data to CSV
    csv_path = 'data/iris.csv'
    df.to_csv(csv_path, index=False)
    logger.info(f"Saved Iris dataset to {csv_path}")
    
    # Log dataset info with MLflow
    with mlflow.start_run(run_name="data_ingestion"):
        mlflow.log_artifact(csv_path, 'dataset')
        mlflow.log_param('dataset_shape', df.shape)
        mlflow.log_param('dataset_columns', df.columns.tolist())
    
    logger.info("Data ingestion completed successfully")

if __name__ == "__main__":
    setup_mlflow()
    ingest_data()