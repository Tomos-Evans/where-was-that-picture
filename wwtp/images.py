"""
Images
"""
from typing import NamedTuple, Iterator


class ImageCollection(NamedTuple):
    location: str
    images: Iterator[str]

