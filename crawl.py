import argparse
from nwc import NaverWebtoonCrawl
import os

parser = argparse.ArgumentParser()
parser.add_argument("--name_en", default="TrueBeauty")  # extra value
parser.add_argument("--no", default="1")
parser.add_argument("--save_dir", default="")

args = parser.parse_args()

if __name__ == "__main__":
    crawler = NaverWebtoonCrawl(args.name_en)
    crawler.save_episode_images(no=args.no)