import requests
import execjs


class en(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }
        self.url = "https://www.endata.com.cn/API/GetData.ashx"

    def get_data(self, year, month):
        data = {
            "startTime": f"{year}-0{month}-01",
            "MethodName": "BoxOffice_GetMonthBox"
        }
        response = requests.post(self.url, headers=self.headers, data=data)
        decryptedData = execjs.compile(open("./en.js", encoding="utf-8").read()).call("decryptData", response.text)
        print(decryptedData)

    def main(self):
        for year in range(2024, 2025):
            for month in range(1, 13):
                self.get_data(year, month)


if __name__ == '__main__':
    en().main()
