import argparse
from nwc import NaverWebtoonCrawl
import os

parser = argparse.ArgumentParser()
parser.add_argument("--name_en", default="TrueBeauty")  # extra value
parser.add_argument("--no", default="1")
parser.add_argument("--save_dir", default="")

args = parser.parse_args()

if __name__ == "__main__":
    if not os.path.exists(f"{args.name_en}/{args.no}/"):
        os.makedirs(f"{args.name_en}/{args.no}/")
    crawler = NaverWebtoonCrawl(args.name_en)
    crawler.save_episode_images(no=args.no)