import argparse
from nwc import NaverWebtoonCrawl
import os

parser = argparse.ArgumentParser()
parser.add_argument("--name_en", default="TrueBeauty")
parser.add_argument("--no", default="1")
parser.add_argument("--all", action="store_true")

args = parser.parse_args()

if __name__ == "__main__":
    crawler = NaverWebtoonCrawl(args.name_en)
    if args.all:
        crawler.save_all_images()
    else:
    crawler.save_episode_images(no=args.no)
