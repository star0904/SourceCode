import re
import requests
import execjs


class maps(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.url = 'https://www.mps.gov.cn/index.html'
        self.js = execjs.compile(open("./mps.js", "r", encoding="utf-8").read())
        self.requests = requests.session()

    def get_cookie(self):
        response = self.requests.get(self.url, headers=self.headers)
        __jsl_clearance_s = execjs.eval(re.findall('document.cookie=(.*?);location.href=', response.text)[0]).split('__jsl_clearance_s=')[-1]
        cookies = {
            '__jsl_clearance_s': __jsl_clearance_s
        }
        response = self.requests.get(self.url, headers=self.headers, cookies=cookies)
        go_code = re.findall(';go\((.*?)\)</script>', response.text)[0]
        __jsl_clearance_s = self.js.call('go', go_code).split('__jsl_clearance_s=')[-1]
        return __jsl_clearance_s

    def get_data(self, __jsl_clearance_s):
        cookies = {
            '__jsl_clearance_s': __jsl_clearance_s
        }
        response = self.requests.get(self.url, headers=self.headers, cookies=cookies)
        response.encoding = 'utf-8'
        print(response.text)

    def main(self):
        __jsl_clearance_s = self.get_cookie()
        self.get_data(__jsl_clearance_s)


if __name__ == '__main__':
    maps().main()
