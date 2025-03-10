import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "client-version": "v2.47.40",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "server-version": "v2025.03.05.1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "e8sgCtaO5NKi0ZqfZacBC7Rs"
}
cookies = {
    "SINAGLOBAL": "8286692417322.23.1740973090306",
    "ULV": "1740973090325:1:1:1:8286692417322.23.1740973090306:",
    "SUB": "_2AkMQmn2Hf8NxqwFRmfAUym7qbIp1zQjEieKmxoxcJRMxHRl-yT9kqlVctRB6OxpTaEXlDVfDXNpPUyXTj_5XbtdC13ut",
    "SUBP": "0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhKzQFZZ_kMxceszoWT49pH",
    "WBPSESS": "fhlE7lUFBip5iXsQIeNCGPN9m4fKsaSuf-t7Pob_B-uLm8A1UFDN7TmLzOY3aHGKZDFTk7bm8ee9AbbyxKbeYnbv2u0TvSTAxLpwKYBSEYpQjTh3yBhDd8wQtIUTGLSPtwA2OYrxUeC4-XzkAbGoTBDCdU9MsaL-D4tTHYQxl4A=",
    "XSRF-TOKEN": "e8sgCtaO5NKi0ZqfZacBC7Rs"
}
url = "https://weibo.com/ajax/feed/hottimeline"
params = {
    "refresh": "2",
    "group_id": "102803",
    "containerid": "102803",
    "extparam": "discover|new_feed",
    "max_id": "1",
    "count": "10"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

# print(response.json())

for i in response.json()["statuses"]:
    items = {}
    items["博主"] = i["user"]["screen_name"]
    items["内容"] = i["text"]
    items["转发量"] = i["reposts_count"]
    items["评论数"] = i["comments_count"]
    items["发表时间"] = i["created_at"]
    print(items)