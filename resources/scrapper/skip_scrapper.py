import json
import requests


class SkipScrapper:
    def __init__(self):
        pass

    def output_to_json_file(self, data):
        with open('../scrapped_data/mcdonalds_menu_skip.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)

    def scrap_restaurant(self):
        url = "https://api-skipthedishes.skipthedishes.com/v1/restaurants/e7b198c0-bef8-4376-8bcb-e7036232c93b/menuitems"
        headers = {"app-token": "d7033722-4d2e-4263-9d67-d83854deb0fc"}
        r = requests.get(url, headers=headers)
        self.output_to_json_file(r.json())


def main():
    skip = SkipScrapper()
    skip.scrap_restaurant()


if __name__ == "__main__":
    main()
