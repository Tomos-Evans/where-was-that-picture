"""
Images
"""
from typing import NamedTuple, Iterator

image_collection_schema: dict = {
    "type": "object",
    "additionalProperties": False,
    "required": ["location", "images"],
    "properties": {
        "location": {"type": "string"},
        "images": {"type": "array", "minItems": 1, "items": {"type": "string"}},
    }
}


class ImageCollection(NamedTuple):
    location: str
    images: Iterator[str]

    @classmethod
    def from_json(cls, config: dict) -> 'ImageCollection':
        """
        Loads and validates the config file
        """
        return ImageCollection(location=config.get("location"), images=config.get("images"))


