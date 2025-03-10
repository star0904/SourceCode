import requests
import execjs
import re


class Bilibili(object):
    def __init__(self):
        self.headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "origin": "https://www.bilibili.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.bilibili.com/video/BV1sy411q7FA/?spm_id_from=333.1007.tianma.2-2-4.click&vd_source=f61da5b60af521b2c9c501c962ef5223",
            "^sec-ch-ua": "^\\^Not/A)Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^126^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.cookies = {
            "buvid3": "5CC793F1-C2A9-28CD-2B80-D4E11F57E5AA55186infoc",
            "b_nut": "1711545355",
            "i-wanna-go-back": "-1",
            "b_ut": "7",
            "_uuid": "1D2951CE-A8AD-C8E2-6858-DFD8F21014ED856494infoc",
            "enable_web_push": "DISABLE",
            "buvid4": "0A655096-DE72-161C-0994-9F905A380E7156255-024032713-nY7rE6ic%2FFrHlaQOZgz0Ss3aC4n2vfI7ptoF0aeD%2B8emEajsXEK4ZIQK5GG79Qbo",
            "header_theme_version": "CLOSE",
            "is-2022-channel": "1",
            "buvid_fp_plain": "undefined",
            "rpdid": "|(k|k)RJk|uu0J'u~uk~l~kl|",
            "DedeUserID": "646714765",
            "DedeUserID__ckMd5": "7c765e0d02905d15",
            "PVID": "1",
            "FEED_LIVE_VERSION": "V_HEADER_LIVE_NEW_POP",
            "CURRENT_QUALITY": "80",
            "SESSDATA": "51bec63a%2C1734606079%2C7fb5e%2A62CjCzGN3n4uDQplvr33Mw-WsW6zDY1YQ4Q6iKssZ4EpQeyhOaHCLw3WhVwEhCB8kZNkASVndXbUY4YTRVMmtRektndjhheGgtTkNhWUZaT0MyTXZfQS1PWnBOZ2piQkhVQV95X0JDeFZQZjFwOF9CWXlPYjFfTFdST1lzZWxVVHZPclJnXzBzMExBIIEC",
            "bili_jct": "a7db3ef3295f2a710a6c043a9cce4ab0",
            "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTkzMTMzMTIsImlhdCI6MTcxOTA1NDA1MiwicGx0IjotMX0.qY0_70s4yfgzA00inQvFOcEVXptAFeILpjSSkJXsP1I",
            "bili_ticket_expires": "1719313252",
            "fingerprint": "bbbcaa1fe72d4bca82955180627c6b29",
            "buvid_fp": "bbbcaa1fe72d4bca82955180627c6b29",
            "bp_t_offset_646714765": "946108383943983104",
            "CURRENT_BLACKGAP": "0",
            "CURRENT_FNVAL": "4048",
            "b_lsid": "E3712EA1_190480FA8B8",
            "home_feed_column": "5",
            "browser_resolution": "1707-791",
            "sid": "6i4akupu"
        }
        self.url = "https://api.bilibili.com/x/v2/reply/wbi/main"
        self.video_url = ["https://www.bilibili.com/video/BV1sy411q7FA/", 'https://www.bilibili.com/video/BV1KS411N7dF/']

    def get_oid(self, video_url):
        params = {
            "spm_id_from": "333.1007.tianma.2-2-4.click",
            "vd_source": "f61da5b60af521b2c9c501c962ef5223"
        }
        response = requests.get(video_url, headers=self.headers, params=params)
        oid = response.text.split('"aid":')[1].split(',')[0]
        return oid

    def get_data(self, oid, page):
        params = {
            "oid": oid,
            "type": 1,
            "mode": 3,
            "pagination_str": '{"offset":"{\\"type\\":1,\\"direction\\":1,\\"data\\":{\\"pn\\":%s}}"}' % page,
            "plat": 1,
            "seek_rpid": "",
            "web_location": 1315875
        }

        cell = execjs.compile(open('bilibili.js', encoding='utf-8').read())
        par = cell.call('formatImgByLocalParams', params)
        params['w_rid'] = par['w_rid']
        params['wts'] = par['wts']
        response = requests.get(self.url, headers=self.headers, params=params, cookies=self.cookies)
        return response.json()

    def parse_data(self, video_url, data, page):
        for j in data['data']['replies']:
            items = {
                '视频链接': video_url,
                '评论页码': page,
                '评论作者': j['member']['uname'],
                '发布时间': j['reply_control']['time_desc'],
                '点赞数': j['like'],
                '评论内容': j['content']['message']
            }
            try:
                items['IP属地'] = re.sub('IP属地：', '', j['reply_control']['location'])
            except KeyError:
                items['IP属地'] = ''

            print(items)

    def main(self):
        for i in range(0, len(self.video_url)):
            oid = self.get_oid(self.video_url[i])
            for page in range(1, 999):
                data = self.get_data(oid, page, )
                if not data['data']['replies']:
                    break
                else:
                    self.parse_data(self.video_url[i], data, page)


if __name__ == '__main__':
    blibili = Bilibili()
    blibili.main()
