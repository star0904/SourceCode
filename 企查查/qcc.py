import requests
import execjs
from urllib.parse import urlparse
import json
import time


class qcc(object):
    def __init__(self):
        self.headers = {
                "content-type": "application/json",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest"
        }
        self.cookies = {
    "QCCSESSID": "705a9588e148d1b057435b59d7",
    "qcc_did": "0d9ffa92-de0c-4578-aaa1-944b1a4c4143",
    "UM_distinctid": "1949dcee66e1137-07d5a5c0eb367d-26001f51-190140-1949dcee66f2130",
    "tfstk": "gRhjCRbsPijjuujoonLzAainrGP1fcOF5Nat-VCVWSFAXG3L4rl2mVEsf0rl0xJgMlCsbVlqbfgG1P3tjEqwoLumo5V9YHr6Tq0DfwQ4Zer9w83uJrLzHcwEB6P9YHRzhwMnZ5nVO8rWF4Eu5rQAHcCR2PE8klCtXue8JySY65n9PuU_l1BYWtBRwPq8X5FtX4L7Sv-MNz8acqTjFdP5HFIolu1O6baJjk3XI1arwrwbvqhf61ULl-ZKkut3SUhTeV2ssNf_DqHnjynADHymWYi7l5OPHW3SBDaoMBSbrxu-8u3CJ630GvGQMxtlESojw7hxdNCtPSZ0ezw5c3ZKi4h3w8RpR4ho0qcS7NdTzDr-ojF69eVbMoF7rf-lMlM-Bjy0siKUnVHSVrNd4v1UAWrhCawh1zZePU6GIW-RJ0dGgyv4Hz4PYUT5c7eYrzT-_U69B-UurGTWP9Rf.",
    "CNZZDATA1254842228": "968798266-1737814370-https%253A%252F%252Fwww.baidu.com%252F%7C1737814420",
    "acw_tc": "0a472f8417378186569625559e0044e816c53cb2ca4f3e2b2e38955447ccac"
}
        self.url = "https://www.qcc.com/api/search/searchMulti"

    def get_data(self, key, page):
        data = {
            "searchKey": key,
            "pageIndex": page,
            "pageSize": 20
        }
        headerEncryption = execjs.compile(open("qcc.js", encoding="utf-8").read()).call("qcc",
                                                                                        urlparse(self.url).path, data)
        print(headerEncryption)
        self.headers[headerEncryption['key']] = headerEncryption['value']
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=data)
        print(response)
        return response.json()

    def main(self):
        key = '万达集团'
        self.get_data(key, i)


if __name__ == '__main__':
    for i in range(1, 146):
        qcc().main()
        time.sleep(1)
