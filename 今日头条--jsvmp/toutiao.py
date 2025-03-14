import requests
import execjs
import time
import urllib.parse


class Toutiao(object):
    def __init__(self):
        self.headers = {
            "referer": "https://www.toutiao.com/?wid=1740055853816",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.cookies = {
            "__ac_signature": "_02B4Z6wo00f01SSphjQAAIDA-NAZgvmlzH0kiYKAAC6g11",
            "tt_webid": "7473482904937563657",
            "gfkadpd": "24,6457",
            "ttcid": "942d0c862595495bad21b87b89c0001e33",
            "local_city_cache": "%E4%B8%AD%E5%B1%B1",
            "csrftoken": "275e2504a726aaa128d46047fff3d8a9",
            "s_v_web_id": "verify_m7dcbw2o_PcLXs3Mv_a9xU_4GsR_8LiO_gAy0sCgiUy1Z",
            "_ga": "GA1.1.1555067876.1740055857",
            "ttwid": "1%7CkC_oncAyxcL46eh3w3USSRGgUoaCW22vM7g1n4ZSsXk%7C1740116099%7C1aaa4fe5fd9c5a149e210aea2b0194b8a1c0cf9fcb513b26721633145d23a79a",
            "_ga_QEHZPBE5HH": "GS1.1.1740115782.6.1.1740116105.0.0.0",
            "tt_scid": "5EaWKJ1jxG1ueQjiIQ7738MmCOilLF5nY6YA-7XH2XUwAQ7Gzy8lYT0LjaL6aLzO77cf"
        }
        self.url = "https://www.toutiao.com/api/pc/list/feed"
        self.params = {
            "channel_id": "0",
            "max_behot_time": str(time.time()).split('.')[0],
            "offset": "0",
            "category": "pc_profile_recommend",
            "aid": "24",
            "app_name": "toutiao_web",
            "msToken": "_YmNVIdrAKvoxVOzrpyeB511l4zyrCj9glYVit8NFX4dKrz5_rwMS792HGxJuXLeifJlfBfzk9NfMKOBsZ9TIGNVjy1ZiThHNnFheaAvJ9FmQvlWZyWXAsIcMUaUaQk=",
        }
        self.js = execjs.compile(open("./toutiao.js", "r", encoding="utf-8").read())

    def get_data(self):
        a_bogus = self.js.call("get_a_bogus", urllib.parse.urlencode(self.params))
        print(a_bogus)
        self.params["a_bogus"] = a_bogus
        response = requests.get(url=self.url, params=self.params, headers=self.headers, cookies=self.cookies)
        print(response.json())

    def main(self):
        self.get_data()


if __name__ == '__main__':
    Toutiao().main()
