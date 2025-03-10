import requests
import json


headers = {
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.xiaohongshu.com",
    "referer": "https://www.xiaohongshu.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    # "x-b3-traceid": "481916802d19a5bd",
    # "x-mns": "awlX3p4fBW0zowEYmXJ/zNNxDEz0Sku52u90/4OKLYw1BG9Z5o3uztDuniPyPMWjvXGGR4Oy5MfpokX3hMpkpIjzzpNHRtIxffPm554O3jzID5w+JLzM6XmL976bBQTjMDgau3x0Qhh8aEm03OYwYZ4y/6J0nf4fXERQyfiC2GxpC7jNR5Ihw6iLu2+7F0+cROT19Pj05QWIi07+oznfJQEO83mLbQ7Jj3Rvd58Z+6HbC20P9I5mKNy0vDd5RbwZKHopctkd17ap6jC1g7zZKB9gxcvmj3tnl5Fom2tMpCGgbXfXLOgt5h7I1BnHN8LNTegkY1FhK5ZCfd/GXNfhwhLMwHnm4w6XhlCTJlhZxTXvCoiFWKW2o0TJWFxtL/6pFfXFR767kzJ4TGIT2159vfDwKf9Q3k99De729DvHDFfxgYkd4f3HPcNW5wyBcXRXyf2F4EZ+NfOO70R128SZQJQEcNmX/QSg4j7ONeFhMLeT6pllRJgeXumMI8mc",
    "x-s": "XYW_eyJzaWduU3ZuIjoiNTYiLCJzaWduVHlwZSI6IngyIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjQzM2IwZDEwOThiYWZhMTg5ZTFhYzA4NmIxZWQ1MzIyOGE3NzA3MDE3ZjU0MTJkNWUwMGZkNDFlZTY1MjYxNTU1NjhkMjkyMzMxMDVkZDk4M2VkOGI2YzM3MDQ4NjcyOWIyM2MyNzYxMjNjMDIxMzUwMDg3MDFlNWQ3YjljYmE5YWQxZGU3NTJjOTI1ZjE3YTFjMmU1NjhlMWUzNDU1ODE4NmQwN2ZjN2E4OTEwZmZlZDc1Y2EyM2Y0MTYxMGViY2M2MDFmNDM3ZDI4ZTAwMDBkODQ0ZjM5MTFjYjIxOTUwNmY2NDIyYzJkM2FkOThlMTA0Y2FlMzE1MGUyODU2ZmIxZTMwZDM2YzBiYzg0MjFlYjk5NmQ0ZTYxNzgyZTMxZDFjNDg5YzU4NzU3N2IzODdhOTY5OTFlOTRiNDExZTIwYjdjNjdhNWNhOTE5ZGUyYTMzZTZiYjdlY2YyMzkyZTQzZDgyZTgxYjg2NDBhNmIwODBlODllYTM1NzcxODdhNDBiZDk3OGVjNzk1ZjZkNzM0ZTEzY2RkNjBlMWJjOTc0In0=",
    # "x-s-common": "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",
    "x-t": "1741408966854",
    # "x-xray-traceid": "caba080c5ce3f082e45c6c58fb9a27b7"
}
cookies = {
    "a1": "19390f4f458t6ijwlhicsz4i63n0h3axojfr7gete50000102075",
    "webId": "f3a53a2670ec6ebc3e920651291b29ef",
    "gid": "yjqj8i2jW8lJyjqj8i4i4Vkd2Y9K3VE1x3SMi9du43KqIF288xq0CW888y8J8W28yyK4KDWi",
    "web_session": "030037a063498e20cd6ed1dfb1204af34f8f88",
}
url = "https://edith.xiaohongshu.com/api/sns/web/v1/homefeed"
data = {
    "cursor_score": "1.741408606946004E9",
    "num": 18,
    "refresh_type": 3,
    "note_index": 89,
    "unread_begin_note_id": "",
    "unread_end_note_id": "",
    "unread_note_count": 0,
    "category": "homefeed_recommend",
    "search_key": "",
    "need_num": 8,
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ],
    "need_filter_image": False
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)