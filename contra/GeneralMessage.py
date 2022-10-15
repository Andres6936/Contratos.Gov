import sys


class GeneralMessage:
    @staticmethod
    def publish(message: str):
        sys.stdout.write(message)

    @staticmethod
    def publishError(message: str):
        sys.stderr.write(message)