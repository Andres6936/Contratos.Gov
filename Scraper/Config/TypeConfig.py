from enum import Enum, unique


@unique
class TypeConfig(Enum):
    INPUT_FOLDER = "InputFolder"
    OUTPUT_FOLDER = "OutputFolder"
