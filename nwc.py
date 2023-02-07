from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from urllib.parse import urlparse, parse_qs
import os
from assets import BASE_LIST_URL, BASE_DETAIL_URL, HEADERS, WEBTOON2CONFIG


class NaverWebtoonCrawl:
    def __init__(self, webtoon_name_en: str):
        assert webtoon_name_en in list(WEBTOON2CONFIG.keys())

        self.webtoon_name_en = webtoon_name_en
        self.webtoon_name_kr = WEBTOON2CONFIG[webtoon_name_en]["name_kr"]
        self.id = WEBTOON2CONFIG[webtoon_name_en]["id"]

    def get_list_html(self, page: int):
        query_params = dict(titleId=self.id, page=page)
        response = requests.get(BASE_LIST_URL, params=query_params, headers=HEADERS)
        html = BeautifulSoup(markup=response.content, features="html.parser")
        return html

    def get_detail_html(self, no: int):
        query_params = dict(titleId=self.id, no=no)
        response = requests.get(BASE_DETAIL_URL, params=query_params, headers=HEADERS)
        html = BeautifulSoup(markup=response.content, features="html.parser")
        return html

    def get_last_episode_no(self):
        html = self.get_list_html(page=1)
        last_episode_url = html.find("td", {"class", "title"}).find("a")["href"]
        parsed_url = urlparse(last_episode_url)
        last_episode_no = int(parse_qs(parsed_url.query)["no"][0])
        return last_episode_no

    def save_episode_images(self, no: int):
        if not os.path.exists(f"{self.webtoon_name_en}/{no}/"):
            os.makedirs(f"{self.webtoon_name_en}/{no}/")

        html = self.get_detail_html(no=no)
        images = html.find("div", {"class", "wt_viewer"}).findAll("img")

        for idx, image in enumerate(tqdm(images)):
            with open(f"{self.webtoon_name_en}/{no}/{idx:03d}.jpg", "wb") as file:
                src = requests.get(image["src"], headers=HEADERS)
                file.write(src.content)

    def save_all_images(self):
        last_no = self.get_last_episode_no()
        for episode_no in range(1, last_no + 1):
            self.save_episode_images(no=episode_no)
