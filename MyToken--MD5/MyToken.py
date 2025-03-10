import requests
import execjs
import time


class MyToken(object):
    def __init__(self):
        self.headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "origin": "https://mytokencap.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://mytokencap.com/",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.url = "https://api.mytokenapi.com/ticker/currencyranklist"

    def get_data(self):
        params = {
            "pages": "1,1",
            "sizes": "100,100",
            "subject": "market_cap",
            "language": "en_US",
            "legal_currency": "USD",
            "timestamp": str((time.time() * 1000)).split('.')[0],
            "platform": "web_pc",
            "v": "0.1.0",
            "mytoken": ""
        }
        returnValue = execjs.compile(open('MyToken.js', encoding='utf-8').read()).call('MyToken')
        print(returnValue)
        params['code'] = returnValue['code']
        params['timestamp'] = returnValue['timestamp']
        response = requests.get(self.url, headers=self.headers, params=params)
        print(response.json())
        return response.json()

    def main(self):
        self.get_data()


if __name__ == '__main__':
    MyToken().main()
