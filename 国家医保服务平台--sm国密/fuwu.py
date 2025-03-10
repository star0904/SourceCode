import requests
import json
import time
import execjs


class fuwu(object):
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Origin": "https://fuwu.nhsa.gov.cn",
            "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }
        self.cookies = {
            "yb_header_active": "-1"
        }
        self.url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital"
        self.js = execjs.compile(open("fuwu.js", "r", encoding="utf-8").read())

    def get_data(self):
        t = {
            "data": {
                "addr": "",
                "regnCode": "110000",
                "medinsName": "",
                "medinsLvCode": "",
                "medinsTypeCode": "",
                "outMedOpenFlag": "",
                "pageNum": 2,
                "pageSize": 10,
                "queryDataSource": "es"
            },
            "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
            "version": "1.0.0",
            "encType": "SM4",
            "signType": "SM2",
            "timestamp": int(str(time.time()).split(".")[0]),
        }
        signData = self.js.call("signData", t)
        encData = self.js.call("encData", t)
        print(signData)
        print('------------------')
        print(encData)

        data = {
            "data": {
                "encData": encData,
            },
            "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
            "version": "1.0.0",
            "encType": "SM4",
            "signType": "SM2",
            "timestamp": t['timestamp'],
            "signData": signData
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=data)
        print(response.text)

    def main(self):
        self.get_data()


if __name__ == '__main__':
    fuwu().main()
