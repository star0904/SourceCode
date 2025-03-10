import requests
import execjs


class login(object):
    def __init__(self):
        self.headers = {
            "content-type": "application/json",
            "origin": "https://seller.kuajingmaihuo.com",
            "referer": "https://seller.kuajingmaihuo.com/login",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.cookies = {
            "api_uid": "CmaweWec4t6NiwBFGuXoAg==",
            "_nano_fp": "Xpmql0Xqn0UYXqEan9_dMeeemleL~fZkeOGQvGGg",
            "_bee": "aaJnmWsyuDODQpcs76IibmLMkzpVsamc",
            "_f77": "206eac0c-f2f3-41d8-8e20-a86da36ed3f4",
            "_a42": "8c272009-2afd-4e3a-ab28-de968bfa5cca",
            "rckk": "aaJnmWsyuDODQpcs76IibmLMkzpVsamc",
            "ru1k": "206eac0c-f2f3-41d8-8e20-a86da36ed3f4",
            "ru2k": "8c272009-2afd-4e3a-ab28-de968bfa5cca"
        }
        self.url = "https://seller.kuajingmaihuo.com/bg/quiet/api/mms/key/login"

    def get_key(self):
        response = requests.post(url=self.url, headers=self.headers, cookies=self.cookies)
        key = response.json()['result']['publicKey']
        return key

    def login(self, key, password):
        encryptPwd = execjs.compile(open("./login.js", encoding="utf-8").read()).call("encrypt", key, password)
        print(encryptPwd)


    def main(self):
        password = "123456"
        key = self.get_key()
        self.login(key, password)


if __name__ == '__main__':
    login().main()
