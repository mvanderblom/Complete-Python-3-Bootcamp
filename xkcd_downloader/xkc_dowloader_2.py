from xkcd_downloader.integration.xkcd_rest_client import XkcdRestClient
from xkcd_downloader.ui.ui_components import Page, Action, Setting

base_url = Setting("http://xkcd.com")
trace = Setting(False)
download_path = Setting("C:\\tmp")

client = XkcdRestClient(base_url, trace)

if __name__ == '__main__':
    print("Welcome to the XKCD downloader")

    settingsPage = Page("Edit settings", [])
    settingsPage.add_action(Action("base_url = {}".format(base_url), lambda: base_url.modify("Enter the new value for base_url: ")))
    settingsPage.add_action(Action(f"trace = {trace}", lambda: trace.modify("Enter the new value for trace: ")))
    settingsPage.add_action(Action(f"download_path = {download_path}", lambda: download_path.modify("Enter the new value for download_path: ")))

    mainPage = Page("What would you like to do?", [])
    mainPage.add_action(Action("edit config", lambda: settingsPage.show()))
    mainPage.add_action(Action("show transcript"))
    mainPage.add_action(Action("download comic"))

    mainPage.show()

    print(base_url)
    print("Thanks for using the XKCD downloader")

