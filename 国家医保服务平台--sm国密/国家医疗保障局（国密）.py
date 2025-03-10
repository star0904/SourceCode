import subprocess
import os


class MySubprocessPopen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        kwargs['encoding'] = "UTF-8"
        super().__init__(*args, **kwargs)


subprocess.Popen = MySubprocessPopen
os.environ["EXECJS_RUNTIME"] = "Node"

import requests
import execjs
import json


class YiBao(object):
    def __init__(self):
        self.cookies = {
            "amap_local": "442000",
            "https_waf_cookie": "5ea0706b-a0f0-45bbd0fe15b1836922cfb91a9d6f778a0270",
            "yb_header_active": "-1"
        }
        self.url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital"
        self.num = 1

    def get_data(self, page):
        headersValue = execjs.compile(open("国家医保服务平台（国密）.js", encoding="utf-8").read()).call("get_headers")
        t = {
            "data": {
                "data": {
                    "addr": "",
                    "regnCode": "442000",
                    "medinsName": "",
                    "medinsLvCode": "",
                    "medinsTypeCode": "",
                    "outMedOpenFlag": "",
                    "pageNum": page,
                    "pageSize": 1000,
                    "queryDataSource": "es"
                },
                "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
                "version": "1.0.0",
                "encType": "SM4",
                "signType": "SM2",
                "timestamp": headersValue['X-Tif-Timestamp']
            }
        }
        dataValue = execjs.compile(open("国家医保服务平台（国密）.js", encoding="utf-8").read()).call("get_data", t)
        headers = {
            'X-Tif-Nonce': headersValue['X-Tif-Nonce'],
            'X-Tif-Paasid': 'undefined',
            'X-Tif-Signature': headersValue['X-Tif-Signature'],
            'X-Tif-Timestamp': str(headersValue['X-Tif-Timestamp']),
            'X-Tingyun': headersValue['X-Tingyun']
        }
        print(dataValue)
        data = {
            "data": {
                "encData": dataValue['encData'],
            },
            "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
            "version": "1.0.0",
            "encType": "SM4",
            "signType": "SM2",
            "timestamp": headersValue['X-Tif-Timestamp'],
            "signData": dataValue['signData']
        }

        response = requests.post(self.url, headers=headers, cookies=self.cookies, data=json.dumps(data))
        return response.json()

    def parse_data(self, response):
        decData = execjs.compile(open("国家医保服务平台（国密）.js", encoding="utf-8").read()).call("decData", response)
        # print(decData)
        for i in decData['list']:
            items = {
                '序号': self.num,
                '医疗机构名称': i['medinsName'],
                '医疗机构编码': i['medinsCode'],
                '医疗机构类型': i['medinsTypeName'],
                '医疗机构等级': i['medinsLvName'],
            }
            try:
                items['医院地址'] = i['addr']
            except KeyError:
                items['医院地址'] = '-'
            self.num += 1
            print(items)

    def main(self):
        for page in range(1, 999):
            print('正在爬取第{}页'.format(page))
            response = self.get_data(page)
            if len(response['data']['data']['encData']) == 544:
                break
            else:
                self.parse_data(response)


if __name__ == '__main__':
    YiBao().main()
