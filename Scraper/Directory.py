from pathlib import Path


class Directory:
    @staticmethod
    def CreateFileIfNotExist(directory: Path) -> None:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
