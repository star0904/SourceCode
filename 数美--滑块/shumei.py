import re
import json
import time
import math
import random
from datetime import datetime
import execjs
import ddddocr
import requests
from typing import List, Tuple
from loguru import logger

requests = requests.Session()


class ShuMei:
    def __init__(self):
        self.headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Origin": "https://www.ishumei.com",
            "Pragma": "no-cache",
            "Referer": "https://www.ishumei.com/trial/captcha.html",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }

        self.rid = ""

    def first_request(self):
        url = "https://captcha1.fengkongcloud.cn/ca/v1/register"
        params = {
            "lang": "zh-cn",
            "appId": "default",
            "captchaUuid": "20250911165908JSy63dcXANKfwJpPtH",
            "rversion": "1.0.4",
            "channel": "default",
            "data": "{}",
            "organization": "d6tpAY1oV0Kv5jRSgxQr",
            "callback": "sm_" + str(time.time_ns() // 1_000_000),
            "model": "slide",
            "sdkver": "1.1.3"
        }
        response = requests.get(url, headers=self.headers, params=params)

        info = json.loads(re.sub(r'^sm_\d+\(|\)$', '', response.text))
        logger.info(info)

        bgUrl = "https://castatic.fengkongcloud.cn" + info["detail"]["bg"]
        fgUrl = "https://castatic.fengkongcloud.cn" + info["detail"]["fg"]
        # logger.info(bgUrl, fgUrl)

        self.rid = info["detail"]["rid"]

        with open("fg.png", "wb") as f:
            f.write(requests.get(fgUrl).content)

        with open("bg.png", "wb") as f:
            f.write(requests.get(bgUrl).content)

    def second_request(self):

        distance = self.slide_distance("./fg.png", "./bg.png")
        trakInfo = self.slide_track(distance)
        track = trakInfo[0]
        passTime = trakInfo[1]
        logger.info("轨迹: {}, 距离：{}px".format(trakInfo, distance))

        Info = execjs.compile(open("./shumei.js", encoding="utf-8").read()).call("getInfo", distance, track, passTime)
        # logger.info(Info)

        url = "https://captcha1.fengkongcloud.cn/ca/v2/fverify"
        params = {
            "captchaUuid": datetime.now().strftime("%Y%m%d%H%M%S") + Info["captchaUuid"],
            "organization": "d6tpAY1oV0Kv5jRSgxQr",
            "callback": "sm_" + str(time.time_ns() // 1_000_000),
            "fm": "BNYA+9sHvZU=",
            "sdkver": "1.1.3",
            "ny": "cvSxP/Xnulg=",
            "bq": "1szrpYdSRZQ=",
            "to": "bftazdO+dKs=",
            "sl": "ld3hnK7eLbY=",
            "rversion": "1.0.4",
            "hg": Info["hg"],  # 轨迹
            "th": Info["th"],  # passTime时间
            "yh": "wFVE7H+kToU=",
            "act.os": "web_pc",
            "ostype": "web",
            "protocol": "185",
            "bs": "buSMMGfrQ6U=",
            "lf": "LCntkg8Oqr0=",  # 背景图高度，固定
            "rid": self.rid,  # 第一次请求返回的rid
            "gg": Info["gg"],  # 滑动距离
            "qt": "QcZFnVbE0HA="  # 背景图宽度，固定
        }
        logger.info(params)
        response = requests.get(url, headers=self.headers, params=params)

        logger.info(response.text)

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
        return int(result['target'][0] / 2)

    @staticmethod
    def slide_track(distance: int) -> Tuple[List[List[int]], int]:
        """
        根据水平滑动距离（像素）生成随机鼠标轨迹
        返回：(轨迹, 总时长/ms)
        首点固定 [0,0,0]，末点 x 严格 == distance
        """
        if distance <= 0:
            return [[0, 0, 0]], 0

        n = random.randint(10, 14)
        t_max = random.randint(1180, 1220)
        y_end = random.randint(-16, -12)
        x_wander = random.randint(6, 10)

        ts = [int(i * t_max / (n - 1)) for i in range(n)]

        ys = [0]
        for i in range(1, n):
            ratio = i / (n - 1)
            y = (1 - 1 / (1 + math.exp(-8 * (ratio - 0.4)))) * y_end
            y += random.randint(-2, 1)
            ys.append(int(round(y)))

        xs = [0]
        for i in range(1, n - 1):
            ratio = i / (n - 1)
            trend = distance * (1 - math.exp(-3 * ratio))
            wander = random.gauss(0, x_wander * (1 - ratio))
            xs.append(int(round(trend + wander)))
        xs.append(distance)

        track = [[int(x), int(y), int(t)] for x, y, t in zip(xs, ys, ts)]
        return track, t_max

    def main(self):
        self.first_request()
        self.second_request()


if __name__ == '__main__':
    sm = ShuMei()
    sm.main()
