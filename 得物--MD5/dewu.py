import requests
import json
import execjs


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://www.dewu.com",
    "Pragma": "no-cache",
    "Referer": "https://www.dewu.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\""
}
cookies = {
    "dw_edge_er_cookie": "c319e9c1-abcd-4719-264f-4907a8d2d74f",
    "sk": "9RXWB9vYn6pbe53doTwpNDQuV7ctGQzmkCEmIVsCvkNqT7uCqUUnf7iQ7F7VrdCb7Zqd6fXUOilnUs95s9rWtH3Poz1z",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22198bc391542d6e-078499ab94671a8-26011051-1821369-198bc3915431c16%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk4YmMzOTE1NDJkNmUtMDc4NDk5YWI5NDY3MWE4LTI2MDExMDUxLTE4MjEzNjktMTk4YmMzOTE1NDMxYzE2In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22198bc391542d6e-078499ab94671a8-26011051-1821369-198bc3915431c16%22%7D"
}
url = "https://app.dewu.com/api/v1/h5/commodity-pick-interfaces/pc/pick-rule-result/category-pick/mapping"

sign = execjs.compile(open("./dewu.js", encoding="utf-8").read()).call("get_sign")

data = {
    "sign": sign,
    "pageNum": 1,
    "pageSize": 20
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)
