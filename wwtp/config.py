"""
Config management
"""
import json
import jsonschema
from typing import NamedTuple, List
from wwtp.images import ImageCollection, image_collection_schema

config_schema: dict = {
  "type": "object",
  "required": ["device_name", "seconds_per_image", "image_collections"],
  "additionalProperties": False,
  "properties": {
    "device_name": {"type": "string"},
    "seconds_per_image": {"type": "integer", "minimum": 5, "maximum": 360},
    "image_collections": {
      "type": "array",
      "items": {"$ref":  "#/definitions/image_collection", "minItems": 1},
    }
  },
  "definitions": {
    "image_collection": image_collection_schema
  }
}


class Config(NamedTuple):
    device_name: str
    image_collections: List[ImageCollection]
    seconds_per_image: int

    @classmethod
    def from_json(cls, config_file_path: str) -> 'Config':
        """
        Loads and validates the config file
        """
        with open(config_file_path, "r") as f:
            config = json.load(f)
        jsonschema.validate(config, config_schema)

        return Config(device_name=config["device_name"],
                      image_collections=[ImageCollection.from_json(c) for c in config.get("image_collections")],
                      seconds_per_image=config.get("seconds_per_image"))


