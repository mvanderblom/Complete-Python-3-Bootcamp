from unittest import TestCase
from unittest.mock import patch

from xkcd_downloader.model.setting import Setting, ModifySettingAction


class TestModifySettingAction(TestCase):

    # @patch('builtins.input', lambda *args: "someNewInput")
    def test_prompt_shows_setting_name_and_value(self):
        s = Setting("Aap")

        msa = ModifySettingAction("Test", "Give me new input: ", s)

        self.assertEqual("Test = Aap", msa.prompt)

    @patch('builtins.input', lambda *args: "someNewInput")
    def test_executing_page_updates_setting(self):
        s = Setting("Aap")

        msa = ModifySettingAction("Test", "Give me new input: ", s)
        msa.execute()

        self.assertEqual("someNewInput", s.value)