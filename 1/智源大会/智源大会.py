import requests
import re
from lxml import etree

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "^cookie": "siteLocale=zh; guidance-2024=yes; hub-live-room-id=27183; hubapi_session=eyJpdiI6IkhlbGgya1lVZ01OTVRYNi9zbEkwdXc9PSIsInZhbHVlIjoiSG9mS3pYRkt1YTdWVlorWWdhbU9aamhHNmE4bWlReFFacHhEempkeGliT2lNd2k2Ymd6YXZDeHZhQ3hDdERqaUVCTlFxTkZPaTQ3Z0IyOG91NHZkOEk3a2tNdllWRnBmM3Z2N1kwTkhnY2cwd2ZzRHRBRWkxQ2ZseUdqWS9sMVUiLCJtYWMiOiJiM2QwMjNjNGQxNzM2NTQ0ZDFkNDRmYTUyNmZhODcxMmJmZmJhNWE0OTRjMmU5N2Q2MjdlYTk2OWIyNGUxMzIyIn0^%^3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImdZdkV5WmVJQ3lNZmZGbVVHSDNHOEE9PSIsInZhbHVlIjoiNW8xa0p1VHRwcWc5NEVvNXdlaE94Q2dqcHZJNXFyTnRyUGphRno5TDBBTExqcTQ2cHNGZzU2dktZL2ZLUytNUS9XVklJV2ZMS0JXc0xyQy9WcEJMeC9uaFNnQkY0Q0ZXSi9idkdkdnJvWktqeFZvbng5cHlBamw2aENWV3AxU3RId1VKUFpMV2lsNGdydE9WblZZVHBRPT0iLCJtYWMiOiJjNTU5OWViMmM0NGY4ZjhjM2RkNTVhMjE4OGJkNDc4ODI5NTIzMzVhMDMyM2E5ZDgxNTY1MGE1OTRiOTAwNjgwIn0^%^3D; SERVERID=6de50b700d45495bd924b6dd9a951ce6^|1718628383^|1718628383^",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "^sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
url = "https://2023.baai.ac.cn/schedule"
response = requests.get(url, headers=headers)

data = etree.HTML(response.text)
num = 1
print(data.xpath('//*[@id="1573721697589940860"]/ul/li[1]/div/div/strong/a /@href'))
print("正在爬取第" + str(num) + "个视频")
for i in data.xpath('//*[@id="1573721697589940860"]/ul/li[1]/div/div/strong/a'):
    vedioUrl = i.xpath('./@href')[0]
    room_id = re.sub(r'.*?id=.*?', '', vedioUrl)
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "^cookie": "p_h5_u=35069033-69CF-4726-A162-5DAEA33D2C70; guidance-2024=yes; hubapi_session=eyJpdiI6InFUZ1JNZGdDc2pRc0NQbWZVRVBtcXc9PSIsInZhbHVlIjoidkNkOGtyTjlGVHZ1SmhrbkdBWXdtOEVUeGZSMGh3UmcyWmRzMlRZM2Z4TFpQdUt3WXY5OUtYRWtGQlFqOEVzeXh2V2NLaWJDenZMb0VGYnlOTDFqOEgrbmdRcEdNeFVaQ0swczh2MzRJWC8rV2NFa3hVWjVxTDc4VGR1elJEeFEiLCJtYWMiOiIwZjc2YWY3MTcwNTI5ZWM0M2E3NGZhZDg4MDE1OGFiNWQwMzQ0NzBlY2VmZmZmM2I3ZTNiMjVmYTFkYWQzZDkxIn0^%^3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImdtNVZ5U1J2Ry9FTFVGZjRWWTVxL2c9PSIsInZhbHVlIjoiMmtic1RJTDFzYXArWEcrYUdOc2FhVzBISXIyeG9FenMyeE0yb21veHFHMGdQTFd3SGUrTnN0U2pFdW9YZUFoc3lEaEhiZkdkekN1eDhNaEVEaHJpSjRWVmNlQTZVYmFhNEk5QUZBSjZ2VjVFcEJtUHZyY3V4bERzWUdqLzFLbHAzUE1vbjIvZE1xV0Z1QlBlc3NnK2d3PT0iLCJtYWMiOiJjZDM2OWQ2Yjg3MGZhZDg2NGQyMzE5ZjQyZDA2OWEyNmVkNTBkNjlkYzVhZGJhMjBjZGUxODRlMDliMmQwYjNiIn0^%^3D; hub-live-room-id=10009090; SERVERID=6de50b700d45495bd924b6dd9a951ce6^|1718629657^|1718623728^",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://2023-live.baai.ac.cn/2023/live/?room_id=10009090",
        "^sec-ch-ua": "^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "^sec-ch-ua-platform": "^\\^Windows^^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    reurl = "https://2023-live.baai.ac.cn/2023/live/api/live-info.json"
    params = {
        "room_id": room_id
    }
    reResponse = requests.get(reurl, headers=headers, params=params)

    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://2023-live.baai.ac.cn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://2023-live.baai.ac.cn/",
        "^sec-ch-ua": "^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "^sec-ch-ua-platform": "^\\^Windows^^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    ts_url = reResponse.json()['body']['source']
    m3u8_text = requests.get(ts_url, headers=headers).text

    m3u8_text = re.sub(r'#E.*', "", m3u8_text)
    sub_ts = ts_url.split("gzc")[0]
    if len(sub_ts) == 146:
        sub = re.sub(r'0102/(.*?).m3u8', '/', sub_ts)
    else:
        sub = re.sub(r'2023(.*?).m3u8', '', sub_ts)
    ts_list = m3u8_text.split()

    for ts in ts_list:
        tsvediourl = sub + ts
        print('视频链接：' + tsvediourl)
        ts_data = requests.get(tsvediourl, headers=headers).content

        with open(f"{num}.ts", mode="ab") as f:
            f.write(ts_data)
    num += 1
