import requests
import json
import execjs


class swGuanCha(object):
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://www.swguancha.com",
            "Pragma": "no-cache",
            "Referer": "https://www.swguancha.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "deviceType": "1",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.url = "https://app.swguancha.com/client/v1/cPublic/consumer/property/rankingList/multi"

    def get_data(self, year, page):
        data = {
            "propertyCode": [
                "DISTRICT_PROP_GJ007_XZQYTDMJ",
                "DISTRICT_PROP_GJ008_JCQMJ",
                "DISTRICT_PROP_GJ010_CSJSYDMJ",
                "DISTRICT_PROP_GJ011_JZYDMJ",
                "DISTRICT_PROP_GJ012_CSJSYDZSQMJBZ"
            ],
            "dimensionTime": f"{year}",
            "orderFieldList": {
                "field": "DISTRICT_PROP_GJ007_XZQYTDMJ",
                "rule": "desc"
            },
            "propertyType": "土地",
            "typeCode": "td",
            "current": page,
            "size": 10,
            "levelType": 2,
            "regionCode": ""
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(self.url, headers=self.headers, data=data)
        decryptedData = execjs.compile(open("./swGuanCha.js", encoding="utf-8").read()).call("decryptData", response.text)
        print(decryptedData)

    def main(self):
        for year in range(2010, 2023):
            for page in range(1, 31):
                self.get_data(year, page)


if __name__ == '__main__':
    swGuanCha().main()
