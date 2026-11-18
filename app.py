import sys

from src.MLProject.logger import logging
from src.MLProject.exceptions import CustomException

if __name__ == "__main__":
    logging.info("Starting the ML Project application...")

    try:
        a=1/0
    except Exception as e:
        logging.info("An error occurred during execution.")
        raise CustomException(e, sys)    