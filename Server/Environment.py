import os
from pathlib import Path


def SetNewVariable(variable: str) -> None:
    (key, value) = variable.split('=')
    os.environ[key] = value


def main() -> None:
    """
    Used for load new environment variables from a file called .secret,
    the variables must be separated for a '=' character
    """
    f = Path('.secret')
    with f.open(mode="r", encoding="utf-8") as f:
        content = f.read()
        variables = content.splitlines()
        for variable in variables:
            SetNewVariable(variable)
