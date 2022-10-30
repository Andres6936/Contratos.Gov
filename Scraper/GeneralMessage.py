import logging


class GeneralMessage:
    @staticmethod
    def publish(message: str):
        logging.info(message)

    @staticmethod
    def publishError(message: str):
        logging.error(message)
