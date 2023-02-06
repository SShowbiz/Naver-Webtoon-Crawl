from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
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

    def save_episode_images(self, no: int):
        html = self.get_detail_html(no=no)
        images = html.find("div", {"class", "wt_viewer"}).findAll("img")
        
        for idx, image in enumerate(tqdm(images)):
            with open(f"{self.webtoon_name_en}/{no}/{idx:03d}.jpg", "wb") as file:
                src = requests.get(image['src'], headers=HEADERS)
                file.write(src.content)