import requests
import execjs
from lxml import etree


class sugh(object):
    def __init__(self):
        self.headers = {
            "Referer": "http://www.sgcc.com.cn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.url = 'http://www.sgcc.com.cn/'
        self.requests = requests.session()

    def get_cookie(self):
        response = self.requests.get(self.url, headers=self.headers)
        # print(response.text)
        content = etree.HTML(response.text).xpath('//meta[2]/@content')[0]
        tsCode = etree.HTML(response.text).xpath('//script[1]/text()')[0]
        functionCode = self.requests.get(
            'http://www.sgcc.com.cn' + etree.HTML(response.text).xpath('//script[2]/@src')[0],
            headers=self.headers).text
        with open('./sgcc.js', encoding='utf-8') as f:
            jsCode = f.read().replace("'content'", content).replace("'tsCode'", tsCode).replace("'functionCode'",
                                                                                                functionCode)
        cookie = execjs.compile(jsCode).call('get_cookie').split(';')[0].split('=')[1]
        return cookie

    def get_data(self, cookie):
        print(cookie)
        cookie = {
            'PW9ydXnjjO8XT': cookie
        }
        response = self.requests.get(self.url, headers=self.headers, cookies=cookie)
        print(response.text)
        print(response)

    def main(self):
        cookie = self.get_cookie()
        self.get_data(cookie)


if __name__ == '__main__':
    sugh().main()
