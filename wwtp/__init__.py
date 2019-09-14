import random
import time
from typing import Tuple
from pychromecast import Chromecast
from wwtp.config import Config
from wwtp.images import ImageCollection


def get_next_image(config: Config) -> Tuple[str, str]:
    """
    Returns the URL of a random image from a random ImageCollection
    """
    image_collection: ImageCollection = random.sample(config.image_collections, 1)[0]
    image: str = random.sample(image_collection.images, 1)[0]
    return image_collection.location, image


def display_next_image(chromecast: Chromecast, config: Config):
    """

    """
    location, image = get_next_image(config)
    chromecast.media_controller.play_media(image, "image/jpeg")
    time.sleep(config.seconds_per_image)
