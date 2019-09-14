"""
TODO: Docstring
"""
import time
import pychromecast
from pychromecast import Chromecast, CAST_TYPE_CHROMECAST
from typing import List


def find_all_chromecasts() -> List[Chromecast]:
    """
    Attempts to find available devices that would be suitable to cast to.
    As we are wanting to display pictures, we will will only include devices that support video.
    ie. Not use Google Audios for example
    """
    return [cc for cc in pychromecast.get_chromecasts() if cc.cast_type == CAST_TYPE_CHROMECAST]


if __name__ == "__main__":
    devices = find_all_chromecasts()
    if not devices:
        raise Exception("No devices to cast to")

    cast = next(cc for cc in devices)
    cast.wait()
    images: List[str] = [
        "https://images.pexels.com/photos/2800724/pexels-photo-2800724.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260",
        "https://images.pexels.com/photos/1774931/pexels-photo-1774931.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        "https://images.pexels.com/photos/2829336/pexels-photo-2829336.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        "https://images.pexels.com/photos/1766478/pexels-photo-1766478.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
    ]

    mc = cast.media_controller
    for image in images:
        mc.play_media(image, "image/jpeg")
        time.sleep(2)

    for cc in devices:
        cc.disconnect()
