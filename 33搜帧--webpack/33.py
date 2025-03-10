import requests
import time
import execjs


class double_three(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.url = "https://fse-api.agilestudio.cn/api/search"

    def get_data(self, page):
        params = {
            "keyword": "火车呼啸而过",
            "page": page,
            "limit": "12",
            "_platform": "web",
            "_versioin": "0.2.5",
            "_ts": str(time.time())
        }
        encrypted = execjs.compile(open("./main.js", encoding="utf-8").read()).call("encrypted", params)
        print(encrypted)
        self.headers["X-Signature"] = encrypted['signature']
        params['_ts'] = encrypted['_ts']
        response = requests.get(self.url, headers=self.headers, params=params)

        print(response.text)

    def main(self):
        for page in range(1, 11):
            self.get_data(page)


if __name__ == '__main__':
    double_three().main()
