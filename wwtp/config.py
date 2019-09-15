"""
Config management
"""
import json
import jsonschema
from typing import NamedTuple

config_schema: dict = {
  "type": "object",
  "required": ["device_name", "seconds_per_image", "server_ip_address"],
  "additionalProperties": False,
  "properties": {
    "device_name": {"type": "string"},
    "seconds_per_image": {"type": "integer", "minimum": 5, "maximum": 360},
    "server_ip_address": {"type": "string"}
  },
}


class Config(NamedTuple):
    device_name: str
    seconds_per_image: int
    server_ip_address: str

    @classmethod
    def from_json(cls, config_file_path: str) -> 'Config':
        """
        Loads and validates the config file
        """
        with open(config_file_path, "r") as f:
            config = json.load(f)
        jsonschema.validate(config, config_schema)

        return Config(device_name=config["device_name"],
                      seconds_per_image=config.get("seconds_per_image"),
                      server_ip_address=config.get("server_ip_address"))


