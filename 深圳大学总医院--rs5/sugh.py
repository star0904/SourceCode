import requests
import execjs
from lxml import etree


class sugh(object):
    def __init__(self):
        self.headers = {
            "Referer": "https://sugh.szu.edu.cn/Html/News/Columns/6/Index.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.url = 'https://sugh.szu.edu.cn/Html/News/Columns/6/Index.html'
        self.requests = requests.Session()

    def get_cookie(self):
        response = self.requests.get(self.url, headers=self.headers)
        content = etree.HTML(response.text).xpath('//meta[2]/@content')[0]
        functionCode = etree.HTML(response.text).xpath('//script[2]/text()')[0]
        tsCode = self.requests.get(
            'https://sugh.szu.edu.cn' + etree.HTML(response.text).xpath('//script[1]/@src')[0]).text
        with open('./sugh.js', encoding='utf-8') as f:
            jsCode = f.read().replace("'content'", content).replace("'functionCode'", functionCode).replace("'tsCode'",
                                                                                                            tsCode)
        cookie = execjs.compile(jsCode).call('get_cookie').split(';')[0].split('=')[1]
        return cookie

    def get_data(self, cookie):
        print(cookie)
        cookies = {
            'ihkYnttrQXfVP': cookie
        }
        response = self.requests.get(self.url, headers=self.headers, cookies=cookies)
        response.encoding = 'utf-8'
        # print(response.text)
        print(response)

    def main(self):
        cookie = self.get_cookie()
        self.get_data(cookie)


if __name__ == '__main__':
    sugh().main()
