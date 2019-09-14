import time
from typing import List
from wwtp.devices import find_all_chromecasts, prepared_chromecast


if __name__ == "__main__":
    images: List[str] = [
        "https://images.pexels.com/photos/2800724/pexels-photo-2800724.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260",
        "https://images.pexels.com/photos/1774931/pexels-photo-1774931.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        "https://images.pexels.com/photos/2829336/pexels-photo-2829336.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        "https://images.pexels.com/photos/1766478/pexels-photo-1766478.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
    ]

    with prepared_chromecast("TV", find_all_chromecasts()) as cc:
        for image in images:
            cc.media_controller.play_media(image, "image/jpeg")
            time.sleep(2)
