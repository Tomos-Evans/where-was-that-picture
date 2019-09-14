"""
Config management
"""
from typing import NamedTuple, List
from wwtp.images import ImageCollection


class Config(NamedTuple):
    device_name: str
    image_collections: List[ImageCollection]
    seconds_per_image: int = 20


