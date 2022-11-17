class Configuration(dict):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
        return cls._instance

    def GetInputFolder(self) -> str:
        return self._instance.inputFolder

    def SetInputFolder(self, inputPath) -> None:
        self._instance.inputFolder = inputPath

    def GetOutputFolder(self) -> str:
        return self._instance.outputFolder

    def SetOutputFolder(self, outputPath) -> None:
        self._instance.outputFolder = outputPath
