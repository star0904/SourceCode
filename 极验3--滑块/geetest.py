import re
import json
import time
import random
from PIL import Image
import execjs
import requests
import ddddocr
from loguru import logger

requests = requests.session()


class GeeTest:
    def __init__(self):
        self.headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://demos.geetest.com/",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Storage-Access": "active",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.gt = ""
        self.challenge = ""
        self.c = []
        self.s = ""
        self.te = ""

        self.jsCode = execjs.compile(open("geetest.js", encoding="utf-8").read())

        self.bg = "./bg.png"
        self.fullBg = "./fullbg.png"
        self.slice = "./slice.png"
        self.sequenceBg = "./sequenceBg.png"
        self.geetest_validate = ""

    # 获取challenge和gt
    def first_request(self):
        url = "https://demos.geetest.com/gt/register-slide"
        params = {
            "t": time.time_ns() // 1_000_000
        }
        response = requests.get(url, headers=self.headers, params=params).json()

        # logger.info(response.text)
        self.challenge = response.get("challenge")
        self.gt = response.get("gt")

    # 获取验证码版本信息，生成第一个w
    def second_request(self):
        url = "https://apiv6.geetest.com/gettype.php"
        params = {
            "gt": self.gt,
            "callback": "geetest_" + str(time.time_ns() // 1_000_000)
        }
        response = requests.get(url, headers=self.headers, params=params)
        info = json.loads(re.sub(r'^geetest_\d+\(|\)$', '', response.text))['data']
        # logger.info(info)
        one = self.jsCode.call("oneW", info, self.gt, self.challenge)
        oneW = one.get("oneW")
        self.te = one.get("te")
        return oneW

    # 获取c和s
    def three_request(self, oneW):
        url = "https://apiv6.geetest.com/get.php"
        logger.info("oneW ===> {}".format(oneW))
        params = {
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "pt": "0",
            "client_type": "web",
            "w": oneW,
            "callback": "geetest_" + str(time.time_ns() // 1_000_000)
        }
        # time.sleep(2)
        response = requests.get(url, headers=self.headers, params=params)
        info = json.loads(re.sub(r'^geetest_\d+\(|\)$', '', response.text))
        # logger.info(info)
        self.c = info['data']['c']
        self.s = info['data']['s']

    # 请求验证码按钮
    def four_request(self):
        twoW = self.jsCode.call("twoW", self.gt, self.challenge, self.te)
        logger.info("twoW ===> {}".format(twoW))

        url = "https://api.geevisit.com/ajax.php"
        params = {
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "pt": "0",
            "client_type": "web",
            "w": twoW,
            "callback": "geetest_" + str(time.time_ns() // 1_000_000)
        }
        # time.sleep(2)
        response = requests.get(url, headers=self.headers, params=params)

        # logger.info(response.text)

    # 获取验证码图片和34位challenge
    def five_request(self):
        url = "https://api.geevisit.com/get.php"
        params = {
            "is_next": "true",
            "type": "slide3",
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "https": "true",
            "protocol": "https://",
            "offline": "false",
            "product": "embed",
            "api_server": "api.geevisit.com",
            "isPC": "true",
            "autoReset": "true",
            "width": "100%",
            "callback": "geetest_" + str(time.time_ns() // 1_000_000)
        }

        response = requests.get(url, headers=self.headers, params=params)

        info = json.loads(re.sub(r'^geetest_\d+\(|\)$', '', response.text))
        # logger.info(info)
        self.challenge = info['challenge']
        bgUrl = "https://static.geetest.com/" + info['bg']
        fullBgUrl = "https://static.geetest.com/" + info['fullbg']
        sliceUrl = "https://static.geetest.com/" + info['slice']

        with open(self.bg, "wb") as f:
            f.write(requests.get(bgUrl).content)
        with open(self.fullBg, "wb") as f:
            f.write(requests.get(fullBgUrl).content)
        with open(self.slice, "wb") as f:
            f.write(requests.get(sliceUrl).content)

        self.c = info['c']
        self.s = info['s']
        self.restore_picture()

    def six_request(self):
        url = "https://api.geevisit.com/ajax.php"
        t = self.slide_distance(self.slice, self.sequenceBg)
        traceInfo = self.slide_track(t)
        trace = traceInfo[0]  # 滑动轨迹
        passTime = traceInfo[1]  # 滑动时间

        # logger.info("trace ===> {}".format(trace))
        # logger.info("passTime ===> {}".format(passTime))
        threeW = execjs.compile(open("three_w.js", encoding="utf-8").read()).call("threeW", self.gt, self.challenge,
                                                                                  passTime, self.te, trace, self.c,
                                                                                  self.s, t)
        logger.info("threeW ===> {}".format(threeW))

        params = {
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "%24_BCm": "0",
            "client_type": "web",
            "w": threeW,
            "callback": "geetest_" + str(time.time_ns() // 1_000_000)
        }
        response = requests.get(url, headers=self.headers, params=params)
        logger.info("滑动距离 ===> {}px, 滑动时间 ===> {}ms".format(t, passTime))

        info = json.loads(re.sub(r'^geetest_\d+\(|\)$', '', response.text))
        logger.info(info)
        self.geetest_validate = info["validate"]

    def login(self):
        url = "https://demos.geetest.com/gt/validate-slide"
        data = {
            "geetest_challenge": self.challenge,
            "geetest_validate": self.geetest_validate,
            "geetest_seccode": self.geetest_validate + "|jordan"
        }
        response = requests.post(url, headers=self.headers, data=data)

        logger.info(response.text)

    # 还原图片
    def restore_picture(self):
        img_list = [self.bg, self.fullBg]
        for index, img in enumerate(img_list):
            image = Image.open(img)
            s = Image.new("RGBA", (260, 160))
            ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43,
                  42,
                  12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
            height_half = 80
            for inx in range(52):
                c = ut[inx] % 26 * 12 + 1
                u = height_half if ut[inx] > 25 else 0
                l_ = image.crop(box=(c, u, c + 10, u + 80))
                s.paste(l_, box=(inx % 26 * 10, 80 if inx > 25 else 0))
            if index == 0:
                s.save(self.sequenceBg)

            else:
                s.save("./sequenceFullBg.png")

    # 模拟轨迹
    @staticmethod
    def __ease_out_expo(sep):
        '''
            轨迹相关操作
        '''
        if sep == 1:
            return 1
        else:
            return 1 - pow(2, -10 * sep)

    def slide_track(self, distance):
        """
        根据滑动距离生成滑动轨迹
        :param distance: 需要滑动的距离
        :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
            x: 已滑动的横向距离
            y: 已滑动的纵向距离, 除起点外, 均为0
            t: 滑动过程消耗的时间, 单位: 毫秒
        """

        if not isinstance(distance, int) or distance < 0:
            raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
        # 初始化轨迹列表
        slide_track = [
            [random.randint(-50, -10), random.randint(-50, -10), 0],
            [0, 0, 0],
        ]
        # 共记录count次滑块位置信息
        count = 10 + int(distance / 2)
        # 初始化滑动时间
        t = random.randint(50, 100)
        # 记录上一次滑动的距离
        _x = 0
        _y = 0
        for i in range(count):
            # 已滑动的横向距离
            x = round(self.__ease_out_expo(i / count) * distance)
            # y = round(__ease_out_expo(i / count) * 14)
            # 滑动过程消耗的时间
            t += random.randint(10, 50)
            if x == _x:
                continue
            slide_track.append([x, _y, t])
            _x = x
        slide_track.append(slide_track[-1])
        return slide_track, slide_track[-1][2]

    @staticmethod
    def slide_distance(slider, bg):
        """
        返回缺口 x 坐标（滑动距离）
        slider/bg: 可以是 URL、本地路径或 data:image/base64 字符串
        """
        ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

        def _load(img):
            # if str(img).startswith('http'):
            #     return requests.get(img).content
            # if str(img).startswith('data:image'):
            #     return base64.b64decode(img.split(',', 1)[-1])
            # 本地文件
            with open(img, 'rb') as f:
                return f.read()

        result = ocr.slide_match(_load(slider), _load(bg), simple_target=True)
        return result['target'][0]

    def main(self):
        self.first_request()
        oneW = self.second_request()
        self.three_request(oneW)
        self.four_request()
        self.five_request()
        self.six_request()
        self.login()


if __name__ == '__main__':
    geetest = GeeTest()
    geetest.main()
