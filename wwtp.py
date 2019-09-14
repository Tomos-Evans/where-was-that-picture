import random
import time
from typing import List
import wwtp
from wwtp.devices import find_all_chromecasts, prepared_chromecast
from wwtp.config import Config
from wwtp.images import ImageCollection


if __name__ == "__main__":
    image_collections: List[ImageCollection] = [
        ImageCollection("random", [
            "https://images.pexels.com/photos/2800724/pexels-photo-2800724.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260",
            "https://images.pexels.com/photos/1774931/pexels-photo-1774931.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        ]),
        ImageCollection("random", [
            "https://images.pexels.com/photos/2829336/pexels-photo-2829336.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
            "https://images.pexels.com/photos/1766478/pexels-photo-1766478.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        ]),
    ]

    config: Config = Config("TV", image_collections, 2)

    with prepared_chromecast(config.device_name, find_all_chromecasts()) as chromecast:
        for _ in range(10):
            wwtp.display_next_image(chromecast, config)
