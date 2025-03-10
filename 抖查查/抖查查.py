import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE3MjMwMzU0NjYsInVzZXJJZCI6MTgxMDI5NzIyMTc3ODkxMTIzMiwiY3JlYXRlRGF0ZSI6IjIwMjQtMDctMDggMjA6NTc6NDYifQ.zc8vImJN8R10xHB1H9Tz8iJk7r3ViRxhP-QbiGwD7Ak",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.douchacha.com",
    "Pragma": "no-cache",
    "Referer": "https://www.douchacha.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "d-t": "1720443587905",
    "d-v": "NSxoQWFmY2RmUXdya1RRTU9UUDhiWXdxODBJak9UUEF6VVBkYkpkc2Yxd3JNRGlzZkJKc2JDd3BuVUxkYnNISGYzSUhmV2FIYm93NjdVclZ3TWR6UE13clF5azFhQ3c3RHJ3NmdUdnlWeGRUVkF3cllVbVVTT3dxV2N3ckhNZGtaTXdyY1VwSGJxdzZ6VE1XR1RQM0NVbkJTcGdVd3d3NXNod3BrVW0xJTJGVU9DUTd3cGNVcXNiRGpIZkRLTE1DdzRPVFBzYnZDOGJXRG5yVE1BWkREV3ZVbzJsTWRUVnN3cnJUb05WemVUVjNmZGJKdzVnVXZ3JTNEJTNE",
    "dcc-href": "https://www.douchacha.com/surge",
    "dcc-r": "https://www.douchacha.com/actualSound",
    "dcc-v": "1.0",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://api.douchacha.com/api/tiktok/ranking/video_list"
params = {
    "ts": "1720443587905",
    "he": "dHb1E3/Un1nUvUaSd8fLwrWeDHfsw57TpdfGwq1Lwq/TqsfHwod=",
    "sign": "e8d457ce79e2ce87",
    "secret": "1103f917bbdcf644b679570e0307565657565e010403554a074556"
}
data = {
    "page_no": 1,
    "page_size": 30,
    "params_data": {
        "ad_fake": False,
        "age": "ALL",
        "creative_video": False,
        "cycle": "H72",
        "digg_count": "ALL",
        "digg_cycle": "H24",
        "duration": "ALL",
        "hot_word": "",
        "keyword": "",
        "label_kind": "",
        "sex": "ALL",
        "with_goods": False,
        "not_gov_media_vip": "",
        "video_type": False
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
