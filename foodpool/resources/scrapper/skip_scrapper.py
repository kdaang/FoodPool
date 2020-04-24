import json
import requests


class SkipScrapper:
    def __init__(self):
        self.app_token = "d7033722-4d2e-4263-9d67-d83854deb0fc"

    def output_to_json_file(self, data, dir, file_name):
        with open("../{}/{}.json".format(dir, file_name), 'w') as f:
            json.dump(data, f, ensure_ascii=False)

    def scrap_skip(self, url, dir, file_name):
        headers = {"app-token": self.app_token}
        r = requests.get(url, headers=headers)
        self.output_to_json_file(r.json(), dir, file_name)

    def scrap_restaurant_menu(self):
        url = "https://api-skipthedishes.skipthedishes.com/v1/restaurants/e7b198c0-bef8-4376-8bcb-e7036232c93b/menuitems"
        self.scrap_skip(url, "scrapped_menu_data", "mcdonalds_menu_skip")

    def scrap_restaurant(self):
        url = "https://api-skipthedishes.skipthedishes.com/v1/restaurants/e7b198c0-bef8-4376-8bcb-e7036232c93b"
        self.scrap_skip(url, "scrapped_restaurant_data", "mcdonalds_restaurant_skip")


def main():
    skip = SkipScrapper()
    # skip.scrap_restaurant_menu()
    skip.scrap_restaurant()


if __name__ == "__main__":
    main()
