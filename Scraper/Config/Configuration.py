class Configuration:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.inputFolder: str = ''
        self.outputFolder: str = ''

    def GetInputFolder(self) -> str:
        return self.inputFolder

    def SetInputFolder(self, inputPath) -> None:
        self.inputFolder = inputPath

    def GetOutputFolder(self) -> str:
        return self.outputFolder

    def SetOutputFolder(self, outputPath) -> None:
        self.outputFolder = outputPath
