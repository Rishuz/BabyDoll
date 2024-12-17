import os

from ..logging import LOGGER


def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove
        elif file.endswith(".jpeg"):
            os.e)
        elif fileswith(".png"):
            os.removee)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("❖ Directories Updated...🧡")
