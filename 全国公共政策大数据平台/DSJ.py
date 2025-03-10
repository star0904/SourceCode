import requests
import execjs


class Dsj(object):
    def __init__(self):
        self.headers = {
            "Content-Type": "application/octet-stream",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.cookies = {
            "Hm_lvt_6146f11e5afab71309b3accbfc4a932e": "1739950490,1739970094",
            "HMACCOUNT": "B83B2E0E0F6DABAA",
            "JSESSIONID": "F732CA9556B2D5B8B503266DC5D21A93",
            "Hm_lpvt_6146f11e5afab71309b3accbfc4a932e": "1739971762"
        }
        self.url = "http://www.spolicy.com/info_api/policyType/showPolicyType"
        self.data = {
            "policyType": "2",
            "province": "",
            "city": "",
            "downtown": "",
            "garden": "",
            "centralId": "",
            "sort": 0,
            "homePageFlag": 1,
            "pageNum": 1,
            "pageSize": 7
        }
        self.js = execjs.compile(open("DSJ.js", "r", encoding="utf-8").read())

    def get_data(self):
        data = self.js.call("get_data", self.data)
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies, data=bytes(data['data']))
        print(response.json())

    def main(self):
        self.get_data()


if __name__ == '__main__':
    dsj = Dsj()
    dsj.main()