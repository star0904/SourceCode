import json
from urllib.parse import unquote
import requests
import execjs


class DouChaCha:
    def __init__(self):
        self.url = "https://api.douchacha.com/api/tiktok/ranking/list_all"

    def get_info(self):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/json;charset=UTF-8",
            "d-t": "1760592893779",
            # "d-v": "NSxYVFVVTnNiSmFMODREZGZpd3J6VUxVOGxVMjNVczFDVE8wVVROUUdVdHNiQndyOTVpeGdVT1lRMldkYm9nTVVVcjhma1ZCblVzU0E0SUhiVHdwaVJ3b2RtSjhicXdwN1Vyc2ZGRDhiZHc2ZUxTc2ZNdzZ0TWN5VnhkTllVcjJXT2RkZlR3cDhDZ0hmOEE4YmJ3cmdUTnNmRXc0NUphc2JCWjhmRUhIYkt3NUNUUUhiS2VOZ1VzUzk5dzY1WXdvT1RNSGJlZENMUEVYUHR3b3NRY1lzT3dvYXBrWUglM0Q=",
            "dcc-href": "https://www.douchacha.com/bloggerRankingFans",
            "dcc-r": "https://www.douchacha.com/",
            "dcc-v": "1.0",
            "origin": "https://www.douchacha.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.douchacha.com/",
            "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
        }
        data = {
            "page_no": 1,
            "page_size": 30,
            "params_data": {
                "label_name": "",
                "period": "DAY",
                "period_value": "20251014"
            }
        }
        info = execjs.compile(open('douchacha.js', encoding='utf-8').read()).call("getInfo", json.dumps(data))
        print(info)

        headers["d-t"] = str(info["ts"])
        params = {
            "ts": info["ts"],
            "he": unquote(info["he"]),
            "sign": info["sign"],
            "secret": info["secret"]
        }
        print(params)
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(self.url, headers=headers, params=params, data=data)

        print(response.text)
        print(response)

    def main(self):
        self.get_info()


if __name__ == '__main__':
    dcc = DouChaCha()
    dcc.main()
