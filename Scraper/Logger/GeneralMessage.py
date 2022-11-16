import logging
from typing import Union


class GeneralMessage:
    logging.basicConfig(
        encoding="utf-8", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S",
        format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    def publish(message: Union[str, object]):
        logging.info(message)

    @staticmethod
    def publishError(message: Union[str, object]):
        logging.error(message)
