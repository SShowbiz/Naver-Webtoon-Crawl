# Naver Webtoon Crawl

## Environment Setting

```shell
$ conda create -n nwc python=3.8
$ pip install requests bs4 pytest-shutil bboxes cvlib
$ pip install argparse tqdm
```

## Running

Add corresponding WEBTOON2CONFIG key and value in assets.py for your interested webtoon. You can find `id` of each webtoon in list view of the url. 

```shell
$ python crawl.py --name_en ${WEBTOON2CONFIG_KEY} --no ${WEBTOON_EPISODE_NO}
```

Above command will save images of specific episode of the webtoon you want.