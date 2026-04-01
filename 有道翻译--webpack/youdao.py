import json
import execjs
import requests


class YouDao:
    def __init__(self):
        with open("./youdao.js", encoding="utf-8") as f:
            js_code = f.read()

        self.ctx = execjs.compile(js_code)

        self.headers = {
            "Origin": "https://fanyi.youdao.com",
            "Referer": "https://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
        }

    def getKey(self):
        url = "https://dict.youdao.com/webtranslate/key"
        params = self.ctx.call("get_params")
        response = requests.get(url, headers=self.headers, params=params)
        # print(response.json())
        secretKey = response.json()['data']['secretKey']
        aesKey = response.json()['data']['aesKey']
        aesIV = response.json()['data']['aesIv']
        return {"secretKey": secretKey, "aesKey": aesKey, "aesIV": aesIV}

    def translation(self, translateWords, key):
        url = "https://dict.youdao.com/webtranslate"

        par = {
            "i": translateWords,
            "from": "auto",
            "to": "",
            "useTerm": False,
            "domain": "0",
            "dictResult": True,
            "keyid": "webfanyi"
        }
        data = self.ctx.call("get_data", par, key["secretKey"])

        # print(data)
        response = requests.post(url, headers=self.headers, data=data)
        # print(response.text)
        decodeData = json.loads(self.ctx.call("decodeData", response.text, key["aesKey"], key["aesIV"]))
        # print(decodeData)
        print("Result:\n", decodeData["translateResult"][0][0]["src"], "==>",
              decodeData["translateResult"][0][0]["tgt"])
        if decodeData["dictResult"]:
            print("Dict:")
            try:
                for i in decodeData["dictResult"]["ce"]["word"]["trs"]:
                    print(i["#tran"], "==>", i["#text"])
            except KeyError:
                for i in decodeData["dictResult"]["ec"]["word"]["trs"]:
                    try:
                        print(i["pos"], "==>", i["tran"])
                    except KeyError:
                        print(i["tran"])

    def main(self):
        key = self.getKey()
        print("输入需要翻译的内容(q退出):")
        translateWords = input("")
        while translateWords != "q":
            self.translation(translateWords, key)
            print("\n输入需要翻译的内容(q退出):")
            translateWords = input("")


if __name__ == '__main__':
    youdao = YouDao()
    youdao.main()
