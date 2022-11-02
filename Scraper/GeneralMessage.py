import logging


class GeneralMessage:
    logging.basicConfig(
        encoding="utf-8", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S",
        format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    def publish(message: str):
        logging.info(message)

    @staticmethod
    def publishError(message: str):
        logging.error(message)
