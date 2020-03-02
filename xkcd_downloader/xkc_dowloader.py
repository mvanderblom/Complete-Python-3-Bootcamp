from xkcd_downloader.integration.xkcd_rest_client import XkcdRestClient


base_url = "http://xkcd.com"
trace = False
download_path = "C:\\tmp"

client = XkcdRestClient(base_url, trace)


def edit_config():
    user_input = ""
    while user_input.upper() != "CR":
        print("Choose the config you want to edit: ")
        print(f"\t - (b)ase_url = {base_url}")
        print(f"\t - (t)race = {trace}")
        print(f"\t - (d)ownload_path = {download_path}")
        print(f"\t - (r)eturn to main menu")
        user_input = "C" + input("")


if __name__ == '__main__':
    print("Welcome to the XKCD downloader")

    user_input = ""
    while user_input.upper() != "Q":
        print("What would you like to do?")
        print("\t - (e)dit config")
        print("\t - (s)how transcript")
        print("\t - (d)ownload comic")
        print("\t - (q)uit")

        user_input = input()
        if(user_input.upper() == "E"):
            edit_config()

    print("Thanks for using the XKCD downloader")

