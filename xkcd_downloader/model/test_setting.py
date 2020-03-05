from unittest import TestCase
from unittest.mock import patch

from xkcd_downloader.model.setting import Setting


class TestSetting(TestCase):

    @patch('builtins.input', lambda *args: "someNewInput")
    def test_modify(self):
        s = Setting("Aap")

        self.assertEqual("Aap", s.value)

        s.modify("Give me new input: ")

        self.assertEqual("someNewInput", s.value)

    def test_string_to_bool_conversion(self):
        self.assertFalse(bool(Setting("Aap")))
        self.assertFalse(bool(Setting("False")))
        self.assertFalse(bool(Setting(False)))
        self.assertTrue(bool(Setting("True")))
        self.assertTrue(bool(Setting(True)))
