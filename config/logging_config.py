# File: mlops-project/config/logging_config.py

import logging

def setup_logging():
    """
    Set up logging configuration.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("mlops.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)