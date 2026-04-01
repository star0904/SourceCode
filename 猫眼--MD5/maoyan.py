import re
import execjs
import requests


class MaoYan:
    @staticmethod
    def first_request():
        uuid = "19909d8ad74c8-0403221978c98e-26011051-1bcab9-19909d8ad75c8"
        print(uuid)
        return uuid

    @staticmethod
    def second_request(uuid):
        finalQuery = execjs.compile(open("./maoyan.js", encoding="utf-8").read()).call("getParams", uuid)
        # print(finalQuery['finalQuery'])
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://piaofang.maoyan.com/dashboard/movie",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        }
        url = "https://piaofang.maoyan.com/dashboard-ajax/movie"
        params = finalQuery["finalQuery"]
        params["WuKongReady"] = "h5"
        print(params)
        response = requests.get(url, headers=headers, params=params)
        response.encoding = "utf-8"

        print(response.text)
        print(response)

    def main(self):
        uuid = self.first_request()
        self.second_request(uuid)


if __name__ == '__main__':
    maoyan = MaoYan()
    maoyan.main()
