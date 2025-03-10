import requests
import execjs
from urllib.parse import urlparse


class QiMai:
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Origin": "https://www.qimai.cn",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.cookies = {
            "qm_check": "A1sdRUIQChtxen8pI0dANi8zcX5zHBl+YnEhLyZIPxw8WkVRVRliYGBFUldeSFk2VEdGX0kQc2gwRk9YAElKBQcACHwAHRghDxUNGw1JcQYDEE9Daw06VkcYCyZPagceEH0DcAlUT0VEWhoSUFRZEgMSBBRVSldESFVKF0o%3D",
            "PHPSESSID": "vv448mc2biu8vr4npr0dqev9hn",
            "gr_user_id": "645a2aed-a206-422b-bded-30c2a2d2c248",
            "ada35577182650f1_gr_session_id": "75908911-fce3-4583-a50e-6d7e629dc380",
            "ada35577182650f1_gr_session_id_sent_vst": "75908911-fce3-4583-a50e-6d7e629dc380",
            "USERINFO": "9qXIfVlos%2BHuIPoNjVeh9a0N4lyjsj11XMSM%2FWCzQ%2F3NMX7ga3vG3ctvkQcjTiakSEiViWCHc3HHQRkmdQFwk67XX8kb1J7SMXNmo%2F6fQgHmCmDIp3FmaHHuJFLCjUR5clvF%2F%2FY97IBCSnLdKQWbgAylGZOSMNR1",
            "AUTHKEY": "iwiwW4RsTqBY6CGpEFxtjT9H%2BQ7ZHCX%2BhPPRuojuolmh9hvEe9RFeg9W4S6YIgjW3cmXyjNvMbQyUOwR47lrskME9dOqkPe%2Blh5whzKiSgxOA8u3JBJwqQ%3D%3D",
            "ada35577182650f1_gr_last_sent_sid_with_cs1": "75908911-fce3-4583-a50e-6d7e629dc380",
            "ada35577182650f1_gr_last_sent_cs1": "qm21646865206",
            "synct": "1737537314.300",
            "syncd": "-2387",
            "ada35577182650f1_gr_cs1": "qm21646865206"
        }
    
    def get_url(self, j):
        url = f"https://api.qimai.cn/rank/indexPlus/brand_id/{j}"
        return url
        
    def get_data(self, page, url):
        params = {
            "brand": "all",
            "device": "iphone",
            "country": "cn",
            "genre": "6014",
            "date": "2025-01-22",
            "page": page
        }
        valuesList = list(params.values())
        analysis = execjs.compile(open("QiMai.js", encoding="utf-8").read()).call("get_analysis", valuesList,
                                                                                  urlparse(url).path)
        print(analysis)
        params['analysis'] = analysis
        response = requests.get(url, headers=self.headers, cookies=self.cookies, params=params)
        print(response.json())
        return response.json()

    def main(self):
        for j in range(0, 3):
            url = self.get_url(j)
            for page in range(1, 11):
                self.get_data(page, url)
            print('-' * 150)


if __name__ == '__main__':
    QiMai().main()
