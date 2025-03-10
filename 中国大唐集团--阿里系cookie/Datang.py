import re
import requests
import execjs


class Datang(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.url = "https://tang.cdt-ec.com/notice/moreController/toMore"

        self.js = execjs.compile(open("./Datang.js", "r", encoding="utf-8").read())

    def get_cookie(self):
        response = requests.get(self.url, headers=self.headers)
        acw_tc = response.cookies.get("acw_tc")
        arg1 = re.findall("var arg1='(.*?)';", response.text)[0]
        arg2 = self.js.call("get_cookie", arg1)
        return acw_tc, arg2

    def get_data(self, acw_tc, arg2):
        cookies = {
            'acw_tc': acw_tc,
            'acw_sc__v2': arg2
        }
        response = requests.get(self.url, headers=self.headers, cookies=cookies)
        print(response.text)

    def main(self):
        acw_tc, arg2 = self.get_cookie()
        self.get_data(acw_tc, arg2)


if __name__ == '__main__':
    Datang().main()
