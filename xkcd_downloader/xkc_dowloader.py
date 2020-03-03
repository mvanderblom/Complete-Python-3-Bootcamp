from xkcd_downloader.integration.xkcd_rest_client import XkcdRestClient
from xkcd_downloader.model.setting import Setting, ModifySettingAction
from xkcd_downloader.ui.ui_components import Page, Action

base_url = Setting("http://xkcd.com")
trace = Setting(False)
download_location = Setting("C:\\tmp")
client = XkcdRestClient(base_url, trace)


def getIntInput():
    user_input = ""
    while not user_input.isnumeric():
        user_input = input("Enter the comic number: ")
    return int(user_input)


def show_transcript():
    meta = client.get_meta(getIntInput())
    print(meta['transcript'])


def download_comic():
    downloaded_path = client.download_image(getIntInput(), str(download_location))
    print(downloaded_path)


if __name__ == '__main__':
    print("Welcome to the XKCD downloader")

    settingsPage = Page("Edit settings", [], "Back")
    settingsPage.add_action(ModifySettingAction("base_url", "Enter the new value for base_url: ", base_url))
    settingsPage.add_action(ModifySettingAction("trace", "Enter the new value for trace: ", trace))
    settingsPage.add_action(ModifySettingAction("download_path", "Enter the new value for download_path: ", download_location))

    mainPage = Page("What would you like to do?", [])
    mainPage.add_action(Action("Edit settings", settingsPage.show))
    mainPage.add_action(Action("Show transcript", show_transcript))
    mainPage.add_action(Action("Download comic", download_comic))

    mainPage.show()

    print("Thanks for using the XKCD downloader")

