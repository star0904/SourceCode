import time
import json
import requests
import execjs


class Geetest:
    def __init__(self):
        self.headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://gt4.geetest.com/",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.cookies = {
            "captcha_v4_user": "33aedd14698b4b15bd0c44509d2a941f",
            "sajssdk_2015_cross_new_user": "1",
            "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219913474595b7c-0193fb396169d76-26011051-1821369-199134745961966%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.geetest.com%2Fadaptive-captcha-demo%22%7D%2C%22%24device_id%22%3A%2219913474595b7c-0193fb396169d76-26011051-1821369-199134745961966%22%7D",
            "Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4": "1756965062",
            "Hm_lpvt_25b04a5e7a64668b9b88e2711fb5f0c4": "1756965062",
            "HMACCOUNT": "B44C478A651898EB"
        }

    def getInfo(self):
        url = "https://gcaptcha4.geetest.com/load"
        challenge = execjs.compile(open("geetest.js", encoding="utf-8").read()).call("uuid")
        # print(challenge)
        params = {
            "callback": "geetest_1756965765174",
            "captcha_id": "54088bb07d2df3c46b79f80300b0abbe",
            "challenge": challenge,
            "client_type": "web",
            "risk_type": "slide",
            "lang": "zh"
        }
        response = requests.get(url, headers=self.headers, cookies=self.cookies, params=params)

        info = json.loads(response.text.strip("geetest_1756965765174(").rstrip(")"))
        # print(info)
        slice_url = "https://static.geetest.com/" + info['data']['slice']
        bg_url = "https://static.geetest.com/" + info['data']['bg']
        # print(slice_url)
        # print(bg_url)

        slice_response = requests.get(slice_url, headers=self.headers, cookies=self.cookies)
        bg_response = requests.get(bg_url, headers=self.headers, cookies=self.cookies)
        with open("slice.png", "wb") as f:
            f.write(slice_response.content)
        with open("bg.png", "wb") as f:
            f.write(bg_response.content)
        info = {
            "lot_number": info['data']['lot_number'],
            "payload": info['data']['payload'],
            "process_token": info['data']['process_token']
        }
        return info

    def verify(self, info):
        # print(info)
        url = "https://gcaptcha4.geetest.com/verify"
        params = {
            "callback": "geetest_" + str(time.time_ns() // 1_000_000),
            "captcha_id": "54088bb07d2df3c46b79f80300b0abbe",
            "client_type": "web",
            "lot_number": info["lot_number"],
            "risk_type": "slide",
            "payload": info["payload"],
            "process_token": info["process_token"],
            "payload_protocol": "1",
            "pt": "1",
            "w": "a745d8b2b45c829c5fba6b3a6b8b6a20453aa39acd299c4018e8f24b51c142db96a74e28434a345a416ef7eae4e35747a7573aa95b7a11c7df513d5585e643945f2b232f65edda2c1c758db0db728c0f847441174de960def77e5443114954ea08b3ab7c5972a472d78850ae70a161ed849ee47266d016d89a34cfb61fdc455bdec5548709232624019d4b37dffa8e73902f34587ce544671a81086e4fa6853e737b83aaebf446001a395f6317b74b2930a2426070f1e7b7db9536a382057068cd730b8371a4cf44d54cd3ecdafb7cb967067eb278871c0ed86ab4b563b32942607262e1fd73896d03baffbccee8b61a50d1aa45ce5f2a680ed45feed479fefa0acbffc8fd7e5cae5e28e7b1e3b7547c72ff74d0c02eae7a35018082a9eb126f5ff64c68974aeccc7876ffd1845d4b6c2a45bb3f34e7ba15f61915a2a36dd07899b5175e7ea1b220ea237e1add655150196e6719f162b6ae7930258186ab8238a61d3cd24c4d4a624ad179028cf9859a39cb2f0a3243f9a9b29a0f41550d0eff547c3cd33e8600539bcb30f0e34e131c4ad795cbe81e61bdcad2725d273e6a648747518507d81bd9e5e54303f9c3b7a5324161b31b7677efc26fb55beb6fd15059a0909493ce8144bc879df660612c97359852c85b06bc3d6f26070e16470fc5a72aef3bcb1ec15385885db05ec32fa499c4ebf68925b488fd19404566c6d306b5ed80ada392e8135ff46c0b43ba61d22c4cafd35766cfcc1bc27043013ae73fe00f605e19f071270cfbf7bd8c10cd14b1c818e6ea4e4a37feac2e15e62ae58ae2d09e276c08f5e296fe48a05594ed939bd3dfa0dcf3ba918a296ed4a7aa627b73e76ff1f6ab14ce02737c2da42809259cf5dff9a961dfc3e4d47ff61fafb6dc4ac24ffb984246f63c5bd1f97cf9bb2c604411d5a9d6e0aa29d892be99717478853dbf5898ede9f04776766e8a07fad147bb17261f00de98d83d37814f15114e57d7ab5cb3e6fe1c476f65dd1a663907dd297b913f2f69b5f0ade8f558546bb90c30f03eb1dfc445099e486c61567d831a2270958a8856cab72b2c41d5c18505"
        }
        print(params)
        # response = requests.get(url, headers=self.headers, cookies=self.cookies, params=params)1

    def main(self):
        info = self.getInfo()
        self.verify(info)


if __name__ == '__main__':
    geetest = Geetest()
    geetest.main()
