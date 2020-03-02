from unittest import TestCase

import responses

from .xkcd_rest_client import XkcdRestClient
from os.path import exists

DOWNLOAD_LOCATION = "C:\\tmp"
DOWNLOADED_FILE = DOWNLOAD_LOCATION + "\\standards.png"


class TestXkcdRestApiClient(TestCase):

    def setUp(self):
        self.client = XkcdRestClient(trace=True)

    def test_get_meta(self):
        meta = self.client.get_meta(420)
        self.assertEqual("Jealousy", meta['title'])

    def test_download_image(self):
        self.client.download_image(927, DOWNLOAD_LOCATION)
        self.assertTrue(exists(DOWNLOADED_FILE))

    @responses.activate
    def test_get_meta_mocked(self):
        responses.add(responses.GET, 'http://xkcd.com/123/info.0.json', json={'aap': 'noot'}, status=200)

        self.client.get_meta(123)

        self.assertTrue(len(responses.calls) == 1)

    @responses.activate
    def test_download_image_mocked(self):
        responses.add(responses.GET, 'http://xkcd.com/123/info.0.json', json={'img': 'http://website/images/aap.png'}, status=200)
        responses.add(responses.GET, 'http://website/images/aap.png', body="")

        self.client.download_image(123, DOWNLOAD_LOCATION)

        self.assertTrue(len(responses.calls) == 2)
