import os
import random
import time
from pychromecast import Chromecast
from wwtp.config import Config


def display_next_image(chromecast: Chromecast, config: Config):
    """
    Finds a random picture from a random location and displays it on the Chromecast.
    """
    location: str = random.sample(os.listdir("/images/"), 1)[0]
    image: str = random.sample(os.listdir(f"/images/{location}"), 1)[0]
    image_url: str = f"http://{config.server_ip_address}:16916/{location}/{image}"
    chromecast.media_controller.play_media(image_url, "image/jpeg")
    time.sleep(config.seconds_per_image)
