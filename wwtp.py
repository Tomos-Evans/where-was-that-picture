import os
import wwtp
from argparse import ArgumentParser
from wwtp.devices import find_all_chromecasts, prepared_chromecast
from wwtp.config import Config


def config_path(path: str):
    if os.path.isfile(path):
        return path
    else:
        raise Exception(f"Could not find config file at: {path}")


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(description='Where was that picture?')
    parser.add_argument('config_path', type=config_path)
    args = parser.parse_args()
    config: Config = Config.from_json(args.config_path)

    with prepared_chromecast(config.device_name, find_all_chromecasts()) as chromecast:
        for _ in range(4):
            wwtp.display_next_image(chromecast, config)
