import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "^Cookie": "_lxsdk_cuid=19073b7fc74c8-0250b7bc309e72-26001f51-190140-19073b7fc74c8; _lxsdk=19073b7fc74c8-0250b7bc309e72-26001f51-190140-19073b7fc74c8; _lxsdk_s=19073b7fc75-525-4aa-6e8^%^7C^%^7C2^",
    "Pragma": "no-cache",
    "Referer": "https://piaofang.maoyan.com/dashboard",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-FOR-WITH": "RRJP6bGlBZoyeRAfnHo0EJbgM0TTuhplbwPkA1mbS72vX9DR5/pEjUddVlBpqPAmeD4exV7F5d9L5gmgYBd8cnZ88wVD9H7xLO7Cpv1uyRMKDV44SqWthXH2xxVRSxAcLHOpcardm7D9ihfxVb4VCtAoCiyBFMr+viKesY34M9uzBuxG4omIVK8KDcq4RtrCQrT/LQ+NbKtfSO+l1zzJPw==",
    "^sec-ch-ua": "^\\^Not/A)Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^126^^, ^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^"
}
url = "https://piaofang.maoyan.com/dashboard-ajax"
params = {
    "orderType": "0",
    "uuid": "19073b7fc74c8-0250b7bc309e72-26001f51-190140-19073b7fc74c8",
    "timeStamp": "1719928374480",
    "User-Agent": "TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2",
    "index": "639",
    "channelId": "40009",
    "sVersion": "2",
    "signKey": "650716b157897f52b5b69e0267a3fe83"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)