from curl_cffi import requests
import execjs


class Akamai:
    def __init__(self):
        self.headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=2",
            "referer": "https://www.dhl.com/cn-zh/home/tracking.html",
            "sec-ch-ua": "\"Chromium\";v=\"135\", \"Not-A.Brand\";v=\"8\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
        }

    def get_home(self, session):
        cookies = {
            "OptanonConsent": "consentId=36828677-ece5-4617-bd59-a9a5c0238ac4&datestamp=Mon+Aug+11+2025+14%3A53%3A15+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202411.1.0&interactionCount=0&isAnonUser=1"
        }
        url = "https://www.dhl.com/cn-zh/home/tracking.html"
        response = session.get(url, headers=self.headers, cookies=cookies)
        # print(response.cookies)
        # print(response.text)
        return response

    def get_request(self, session):
        url = "https://www.dhl.com/a8DL/d5--/ec4/L7Y/imlw/N9r5fkmS2QNhfccO/WWdFNA/eQQ/xLUV5FE8B"
        response = session.get(url, headers=self.headers)
        # print(response.text)

        cookies_str = '; '.join([f"{k}={v}" for k, v in response.cookies.items()])

        # print(cookies_str)
        return cookies_str

    def post_request(self, session, cookies_str):
        with open("./akamai.js", "r", encoding="utf-8") as f:
            jsCode = f.read()

        jsCode = "oldCookie=\'" + cookies_str + '\';\n' + jsCode
        # print(jsCode)


        sensor_data = execjs.compile(jsCode).call("get_sensor_data")
        print(sensor_data)

        url = "https://www.dhl.com/a8DL/d5--/ec4/L7Y/imlw/N9r5fkmS2QNhfccO/WWdFNA/eQQ/xLUV5FE8B"
        response = session.post(url, headers=self.headers, data=sensor_data)
        print(response.cookies)
        print(response)
        print(response.text)

    def main(self):
        with requests.Session() as session:
            self.get_home(session)
            cookies_str = self.get_request(session)
            self.post_request(session, cookies_str)


if __name__ == '__main__':
    akamai = Akamai()
    akamai.main()
