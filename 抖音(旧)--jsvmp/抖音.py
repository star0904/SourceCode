import requests
import execjs
import urllib.parse
import datetime


class Douyin(object):
    def __init__(self):
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.douyin.com/?recommend=1",
            "^sec-ch-ua": "^\\^Not/A)Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^126^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        self.cookies = {
            "ttwid": "1%7CnZHtcWsB1Zqbzxto6CtDaEcocsxWPvQrjrdi7skg64s%7C1710334542%7Cbd875f594ab3f30fc0f4d60b129e39906f96ac0a467f497611c68322a0ea109e",
            "bd_ticket_guard_client_web_domain": "2",
            "xgplayer_user_id": "768459716868",
            "SEARCH_RESULT_LIST_TYPE": "%22single%22",
            "UIFID_TEMP": "3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c274cc95e53937360a4405c08fa8b2a5d503305204529f4485c05970838253e44d416803814b0401e9e8d7ae34db44cae4",
            "fpk1": "U2FsdGVkX19DKLbROIFcIfdQFa5I1dpskbSUUS+P/87kauC1xRNjE70DOwa8iMi7qlqK6ox5gr/rNplhNTKBHw==",
            "fpk2": "f1f6b29a6cc1f79a0fea05b885aa33d0",
            "s_v_web_id": "verify_lxlulwfh_V0oRdiTP_BGMe_4usX_AtKf_iMcjqNXkSQhR",
            "passport_csrf_token": "22c7c874a6bf907859356b974e8c7022",
            "passport_csrf_token_default": "22c7c874a6bf907859356b974e8c7022",
            "UIFID": "3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c2cade638c223dff894662ad9d27090e65be542822ae89c0673b1c6bfb1e261ab997b7ebdc067c40fa9b283e3af2706ace2b1c9879d31aa714d635981a2db0d1a3c362ec2709fb91c467e182b037c1156930cf5c6a1bf5ef202937fa78a9c1d464e8ac8923bb1fe69247cf8f787cb0b54e1ec8603fcb3d91062d93dc315f404858",
            "n_mh": "PTYmBdyteFCGnlxsUPrsJLArYGiRrSBB_mQdmSpo99w",
            "_bd_ticket_crypt_doamin": "2",
            "__security_server_data_status": "1",
            "store-region": "cn-gd",
            "store-region-src": "uid",
            "xgplayer_device_id": "18080060252",
            "my_rd": "2",
            "passport_assist_user": "CkGppOXf3uUVBAx7wwVWl0HIne0Orw1nKpn4T5C7V41yVXFDH_gpg3ohjOIJJO-ej_zWeNr3MiQhoQWGlgFW0Ro_QhpKCjx3TA5fo9KIL0Y-g5nJtog-gmjLPrCACYweG2bQLWGtRuEjdG6uP2s-zK4oxk6tX-GQCn-3cPw_UqRwIa0Q4JrWDRiJr9ZUIAEiAQPcVBxe",
            "sso_uid_tt": "fc2ce1fa7a827c23e99040f5e18d162d",
            "sso_uid_tt_ss": "fc2ce1fa7a827c23e99040f5e18d162d",
            "toutiao_sso_user": "d5d94f5f0c282e9d2a1e474fdf7a01cc",
            "toutiao_sso_user_ss": "d5d94f5f0c282e9d2a1e474fdf7a01cc",
            "sid_ucp_sso_v1": "1.0.0-KGVlY2Q2YzE1MTFiZTk2YzZjZjBmZTBlNzI3Y2NlYzYzZDIxZDY2N2YKIQijxICJr_XIBxDkjLW0BhjvMSAMMO2nvOUFOAZA9AdIBhoCbGYiIGQ1ZDk0ZjVmMGMyODJlOWQyYTFlNDc0ZmRmN2EwMWNj",
            "ssid_ucp_sso_v1": "1.0.0-KGVlY2Q2YzE1MTFiZTk2YzZjZjBmZTBlNzI3Y2NlYzYzZDIxZDY2N2YKIQijxICJr_XIBxDkjLW0BhjvMSAMMO2nvOUFOAZA9AdIBhoCbGYiIGQ1ZDk0ZjVmMGMyODJlOWQyYTFlNDc0ZmRmN2EwMWNj",
            "passport_auth_status": "e6ced054769b2c254daac3b7d94835d6%2Cdd2fb580c00ec74cc762288a071d4f17",
            "passport_auth_status_ss": "e6ced054769b2c254daac3b7d94835d6%2Cdd2fb580c00ec74cc762288a071d4f17",
            "uid_tt": "2b5c01ced9949ae3f33f08c34a8dc86b",
            "uid_tt_ss": "2b5c01ced9949ae3f33f08c34a8dc86b",
            "sid_tt": "252f666a881c09f2ce88b07febe904d6",
            "sessionid": "252f666a881c09f2ce88b07febe904d6",
            "sessionid_ss": "252f666a881c09f2ce88b07febe904d6",
            "_bd_ticket_crypt_cookie": "bcbd64c5ca4159b05086f09d36eed314",
            "sid_guard": "252f666a881c09f2ce88b07febe904d6%7C1720534634%7C5183997%7CSat%2C+07-Sep-2024+14%3A17%3A11+GMT",
            "sid_ucp_v1": "1.0.0-KDhkM2IzOTI3NDFkMjUzMTFmMjM3YTFhNDM4YWY5MmNmYzZhODEwNjEKGwijxICJr_XIBxDqjLW0BhjvMSAMOAZA9AdIBBoCbGYiIDI1MmY2NjZhODgxYzA5ZjJjZTg4YjA3ZmViZTkwNGQ2",
            "ssid_ucp_v1": "1.0.0-KDhkM2IzOTI3NDFkMjUzMTFmMjM3YTFhNDM4YWY5MmNmYzZhODEwNjEKGwijxICJr_XIBxDqjLW0BhjvMSAMOAZA9AdIBBoCbGYiIDI1MmY2NjZhODgxYzA5ZjJjZTg4YjA3ZmViZTkwNGQ2",
            "dy_swidth": "1707",
            "dy_sheight": "960",
            "publish_badge_show_info": "%220%2C0%2C0%2C1722219659499%22",
            "live_use_vvc": "%22false%22",
            "download_guide": "%223%2F20240729%2F0%22",
            "pwa2": "%220%7C0%7C3%7C0%22",
            "volume_info": "%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.204%7D",
            "douyin.com": "",
            "device_web_cpu_core": "20",
            "device_web_memory_size": "8",
            "architecture": "amd64",
            "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22",
            "csrf_session_id": "d24b4fa868364e7aa820c3507bd847ec",
            "strategyABtestKey": "%221722391538.338%22",
            "biz_trace_id": "db966edb",
            "passport_fe_beating_status": "true",
            "FOLLOW_NUMBER_YELLOW_POINT_INFO": "%22MS4wLjABAAAAlQrGsYdzk3g6UMNIp7aZeTAql0qRRtFqnWHhiWP8RAV2hIVi9yaVH5vLrW42zdcr%2F1722441600000%2F0%2F0%2F1722396844003%22",
            "WallpaperGuide": "%7B%22showTime%22%3A1722260128911%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A21%2C%22cursor2%22%3A0%7D",
            "__ac_nonce": "066a9c8490050579e5fe0",
            "__ac_signature": "_02B4Z6wo00f01lY53nAAAIDDikBBxkFJNtpWGdrAAPM27WtH5JH42.MhXTBa5I8AF8Re0VofmL1fZvAj51BHUk2aLN9PX2-rlpcvgzv37RE-q.oDmYoETWmIQIBsCtXennRDIlTduMefYWZ-82",
            "IsDouyinActive": "true",
            "FOLLOW_LIVE_POINT_INFO": "%22MS4wLjABAAAAlQrGsYdzk3g6UMNIp7aZeTAql0qRRtFqnWHhiWP8RAV2hIVi9yaVH5vLrW42zdcr%2F1722441600000%2F0%2F1722402892001%2F0%22",
            "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQjFLa2M2ZGEzYnhvMXUxQ3kzbDJlZFVadFlRV3VuSTlQM2tMczhOTUtiaHdhUDFUamtwVThIV0pJQ2VoVU9TYkVrd2ZJb3hCb3gveEE1V0xGakRJaVk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D",
            "xg_device_score": "7.646410827714261",
            "stream_player_status_params": "%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22",
            "home_can_add_dy_2_desktop": "%221%22",
            "odin_tt": "01829355a7773775943c31abe976258301e65b11c5d0467036b8b7113b09f84ab104fb56e932dbf7213961a4a6abdd3e"
        }
        self.url = "https://www.douyin.com/aweme/v1/web/comment/list/"

    def get_data(self, page):
        params = {
            "device_platform": "webapp",
            "aid": "6383",
            "channel": "channel_pc_web",
            "aweme_id": "7397634606486342922",
            "cursor": str(page * 50),
            "count": "50",
            "item_type": "0",
            "insert_ids": "",
            "whale_cut_token": "",
            "cut_version": "1",
            "rcFT": "",
            "update_version_code": "170400",
            "pc_client_type": "1",
            "version_code": "170400",
            "version_name": "17.4.0",
            "cookie_enabled": "true",
            "screen_width": "1707",
            "screen_height": "960",
            "browser_language": "zh-CN",
            "browser_platform": "Win32",
            "browser_name": "Chrome",
            "browser_version": "126.0.0.0",
            "browser_online": "true",
            "engine_name": "Blink",
            "engine_version": "126.0.0.0",
            "os_name": "Windows",
            "os_version": "10",
            "cpu_core_num": "20",
            "device_memory": "8",
            "platform": "PC",
            "downlink": "10",
            "effective_type": "4g",
            "round_trip_time": "50",
            "webid": "7345830874325288488",
            "msToken": "CCMi1At0h_-S4P0DR0eHBvYnFsnJzrFpCFPiRRq0lVHilkLHc9R-WZmWBtUYsnikXsGfLRcBoMGLndGtJxH7QwpatPysytlRxnBq21fvaZhRflh0BQPvxFEvJ50Y",
            "verifyFp": "verify_lxlulwfh_V0oRdiTP_BGMe_4usX_AtKf_iMcjqNXkSQhR",
            "fp": "verify_lxlulwfh_V0oRdiTP_BGMe_4usX_AtKf_iMcjqNXkSQhR^"
        }
        params_str = urllib.parse.urlencode(params)
        a_bogus = execjs.compile(open("抖音.js", encoding="utf-8").read()).call("get_a_bogus", params_str)
        print(a_bogus)
        params['a_bogus'] = a_bogus
        response = requests.get(self.url, headers=self.headers, params=params, cookies=self.cookies)
        return response.json()

    def parse_data(self, response):
        for i in response['comments']:
            items = {
                "评论内容": i['text'],
                "评论用户": i['user']['nickname'],
                "ip属地": i['ip_label'],
                '点赞数': i['digg_count'],
                '评论时间': datetime.datetime.fromtimestamp(i['create_time']).strftime('%Y-%m-%d %H:%M:%S')
            }
            print(items)

    def main(self):
        for page in range(0, 999):
            response = self.get_data(page)
            if response.get('comments') is None:
                break
            else:
                self.parse_data(response)


if __name__ == '__main__':
    Douyin().main()
