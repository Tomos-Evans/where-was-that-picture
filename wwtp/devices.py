"""
Manages castable devices - currently only Chromecasts
"""
from contextlib import contextmanager

import pychromecast
from pychromecast import Chromecast, CAST_TYPE_CHROMECAST
from typing import List, ContextManager


def find_all_chromecasts() -> List[Chromecast]:
    """
    Attempts to find available devices that would be suitable to cast to.
    As we are wanting to display pictures, we will will only include devices that support video.
    ie. Not use Google Audios for example
    """
    return [cc for cc in pychromecast.get_chromecasts() if cc.cast_type == CAST_TYPE_CHROMECAST]


@contextmanager
def prepared_chromecast(friendly_name: str, all_devices: List[Chromecast]) -> ContextManager[Chromecast]:
    """
    Context manager used to prepare the desired chromecast, and clean up afterwards.
    """
    cast: Chromecast = next(cc for cc in [d for d in all_devices if d.device.friendly_name == friendly_name])
    cast.wait()

    yield cast

    for cc in all_devices:
        cc.disconnect()
