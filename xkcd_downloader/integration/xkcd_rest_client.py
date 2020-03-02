import requests
import json


class XkcdRestClient():
    def __init__(self, base_url="http://xkcd.com", trace=False):
        self.base_url = base_url
        self.trace = trace

    def get_meta(self, comic_id):
        return self.__get_json(self.base_url + "/{comicId}/info.0.json".format(comicId=comic_id))

    def download_image(self, comic_id, download_location):
        meta = self.get_meta(comic_id)

        img_url = meta['img']
        img_file_name = img_url[img_url.rfind('/') + 1:]
        file_path = download_location + "\\" + img_file_name

        if self.trace:
            print("Downloading image {} to {}".format(img_url, file_path))

        with open(file_path, 'wb+') as img_file:
            img_file.write(requests.get(img_url).content)

    def __get_json(self, url):
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()

        if self.trace:
            print("GET " + url)
            print(json.dumps(response_json, indent=4, sort_keys=True))

        return response_json
