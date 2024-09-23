import os
import sys
import pandas as pd
from sklearn.datasets import load_iris
import mlflow

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.config.mlflow_config import setup_mlflow
from src.config.logging_config import setup_logging

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
    csv_path = os.path.join(project_root, 'data', 'iris.csv')
    df.to_csv(csv_path, index=False)
    logger.info(f"Saved Iris dataset to {csv_path}")
    
    # Log dataset info with MLflow
    mlflow.set_experiment("data_ingestion")
    with mlflow.start_run(run_name="iris_data_ingestion"):
        mlflow.log_artifact(csv_path, 'dataset')
        mlflow.log_param('dataset_shape', df.shape)
        mlflow.log_param('dataset_columns', df.columns.tolist())
    
    logger.info("Data ingestion completed successfully")

if __name__ == "__main__":
    setup_mlflow()
    ingest_data()