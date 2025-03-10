import json
import os
import requests
import execjs

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "vinfo_n_f_l_n3=477558a0d3c671c9.1.0.1718107507606.0.1718107532250; NMTID=00Of1w5v6Zo0kWLxURkty5N_yRLvZMAAAGQJecLpQ; _iuqxldmzr_=32; _ntes_nnid=be9bf77f6c53644a6f440fb99c68a4e3,1718622817648; _ntes_nuid=be9bf77f6c53644a6f440fb99c68a4e3; WEVNSM=1.0.0; WNMCID=pzxbqu.1718622817942.01.0; WM_TID=GdyGiY26CodBABBQVReGEAky^%^2FC9E7woR; ntes_utid=tid._.liqOKBcN1^%^252FJAR1RFFUeXFAxzqX4CL7^%^252B8._.0; sDeviceId=YD-h6LTyMpYvuJBRgVFAEOF2szJe8Tx7Xob; __snaker__id=7fKGd4a4XHh6G01Q; gdxidpyhxdE=CgdNLb3EglBznJv5ijQjpi^%^2BsJarc33^%^2FZP9Nl9aR^%^5C8I^%^2BmvDdn92fSAw363rO^%^5CSd6JiwPc4jTpd1YnkE9vn4UsS85^%^5CUEXkZd48eLCvgJ6^%^2BY6K3A5f0AYYippC^%^2FHPkotqYWcKRGMvtoKBg^%^5CCQ59Q7ICAceyeVDHAGUsK^%^2B^%^2F8IT2A^%^5CWoNeyuS^%^3A1718623752272; MUSIC_U=00208474FB151E4ABAF025817843C86F1927F5C6A079321EC009A1A02DF0AB7B290378E6D762D359F186DA793EC23962B7074820049F5BEADD2928B241D98FBB1CDE04B2AB4E16753E5F1445D3F160431CB0CFF34FB8DF00BE7F51436EF766DA9557721458A4B80E0A88BCB7CF81F9BD27A74CBED4C2675ED53714F01103B6A0AB34DD7F120BE1013597D2F5439C408A1CF2A674D4970DB1C579B103605FF811D93458EE5D67ED6FE05B70AE5A8E05E745909F77F972B3E59BAC04FA0F9FE10596401CE5532B59D413E8BD92B1EBE7918ADE503121F8773CE751AB78F11186A219575B033D977887082C6182EDF935E077ED11F119B0B6698F638C305C4A2694056CE6E7E6000B6F007F573B380F1FF927C2F39C557647005B6E8D49E18DD6425792DC24CD5484CE60AB00EAD61E9B0B85E5B88595101DA27E9544D001B8E3F0C38E29751F1ADF779B5AC717D9C62ECCFA200B409188FBEC60405D43D8F6AE505C; __csrf=a957962f952014c5ba2fd7c5424424fb; ntes_kaola_ad=1; WM_NI=5xEFJp8OO29tzPnX355Ft^%^2BLrf^%^2BMVA6k^%^2FdDd9rsznrvQ5EvLZM^%^2FJCDe7adbSt60^%^2Fdge^%^2FlrJu10WokVr88cHhiLwf0xqEbMf^%^2BnbxBp4c4YCzHO75SD8V4p4UZJFktHkSrAUnU^%^3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed0d241a2aca295dc6488868fb3d45e839f8f86cb4e87ee879ab159f8a8bad8c62af0fea7c3b92af7a88ba7c97cfc9181d3bc80ba90a2b9b23ff79abccccf7aa6f583b7c43ea9f1aca5e733b2adb68ff17e93eb8b97cf528ff186a4c76ff5bfac83d280f6f0e185e66fedb4beabf83bf489a18cd57afce8ada9eb6390a9aad1fb7b87be8387aa66a2a88e91b769f8878d9bcb45f5eb9da5bb5ef8b0fcb6d94286b5bca9ea59b29f9b8fd837e2a3; playerid=41805395; JSESSIONID-WYYY=BIb^%^2BHwcEKQcR8iNFDUzBo^%^2BBWUKKlnGfbXCBBnwCoaNHF9^%^5CQj^%^2F1EDFvbww^%^2FXSv0HPXnqnrb1dcJ7ZTMuoVCcOnggW0y8eJ^%^5CzXQ6IEpCn8yBPJDRg6o3gSUPthHSCkRypOCRhM4^%^2FwZxed^%^2B3nWQgJPM5AcHTAS7tcdKulxAQwjvMdIUylKy^%^3A1718721889529^",
    "nm-gcore-status": "1",
    "origin": "https://music.163.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://music.163.com/search/",
    "sec-ch-ua": "^\\^Not/A)Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^126^^, ^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
url = "https://music.163.com/weapi/cloudsearch/get/web"
params = {
    "csrf_token": "a957962f952014c5ba2fd7c5424424fb"
}

aa = {
    "hlpretag": "<span class='s-fc7'>",
    "hlposttag": "</span>",
    "s": "周杰伦",
    "type": "1",
    "offset": "0",
    "total": "true",
    "limit": "30",
    "csrf_token": "a957962f952014c5ba2fd7c5424424fb"
}
cell = execjs.compile(open("网易云.js", encoding="utf-8").read()).call("get_data", json.dumps(aa))
data = {
    "params": cell.get("encText"),
    "encSecKey": cell.get("encSecKey")
}
response = requests.post(url, headers=headers, params=params, data=data)

# print(response.json())

for i in response.json()['result']['songs']:
    items = {
        'name': i['name']
    }
    Id = i['id']

    reHeaders = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "^cookie": "vinfo_n_f_l_n3=477558a0d3c671c9.1.0.1718107507606.0.1718107532250; NMTID=00Of1w5v6Zo0kWLxURkty5N_yRLvZMAAAGQJecLpQ; _iuqxldmzr_=32; _ntes_nnid=be9bf77f6c53644a6f440fb99c68a4e3,1718622817648; _ntes_nuid=be9bf77f6c53644a6f440fb99c68a4e3; WEVNSM=1.0.0; WNMCID=pzxbqu.1718622817942.01.0; WM_TID=GdyGiY26CodBABBQVReGEAky^%^2FC9E7woR; ntes_utid=tid._.liqOKBcN1^%^252FJAR1RFFUeXFAxzqX4CL7^%^252B8._.0; sDeviceId=YD-h6LTyMpYvuJBRgVFAEOF2szJe8Tx7Xob; __snaker__id=7fKGd4a4XHh6G01Q; gdxidpyhxdE=CgdNLb3EglBznJv5ijQjpi^%^2BsJarc33^%^2FZP9Nl9aR^%^5C8I^%^2BmvDdn92fSAw363rO^%^5CSd6JiwPc4jTpd1YnkE9vn4UsS85^%^5CUEXkZd48eLCvgJ6^%^2BY6K3A5f0AYYippC^%^2FHPkotqYWcKRGMvtoKBg^%^5CCQ59Q7ICAceyeVDHAGUsK^%^2B^%^2F8IT2A^%^5CWoNeyuS^%^3A1718623752272; MUSIC_U=00208474FB151E4ABAF025817843C86F1927F5C6A079321EC009A1A02DF0AB7B290378E6D762D359F186DA793EC23962B7074820049F5BEADD2928B241D98FBB1CDE04B2AB4E16753E5F1445D3F160431CB0CFF34FB8DF00BE7F51436EF766DA9557721458A4B80E0A88BCB7CF81F9BD27A74CBED4C2675ED53714F01103B6A0AB34DD7F120BE1013597D2F5439C408A1CF2A674D4970DB1C579B103605FF811D93458EE5D67ED6FE05B70AE5A8E05E745909F77F972B3E59BAC04FA0F9FE10596401CE5532B59D413E8BD92B1EBE7918ADE503121F8773CE751AB78F11186A219575B033D977887082C6182EDF935E077ED11F119B0B6698F638C305C4A2694056CE6E7E6000B6F007F573B380F1FF927C2F39C557647005B6E8D49E18DD6425792DC24CD5484CE60AB00EAD61E9B0B85E5B88595101DA27E9544D001B8E3F0C38E29751F1ADF779B5AC717D9C62ECCFA200B409188FBEC60405D43D8F6AE505C; __csrf=a957962f952014c5ba2fd7c5424424fb; ntes_kaola_ad=1; WM_NI=5xEFJp8OO29tzPnX355Ft^%^2BLrf^%^2BMVA6k^%^2FdDd9rsznrvQ5EvLZM^%^2FJCDe7adbSt60^%^2Fdge^%^2FlrJu10WokVr88cHhiLwf0xqEbMf^%^2BnbxBp4c4YCzHO75SD8V4p4UZJFktHkSrAUnU^%^3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed0d241a2aca295dc6488868fb3d45e839f8f86cb4e87ee879ab159f8a8bad8c62af0fea7c3b92af7a88ba7c97cfc9181d3bc80ba90a2b9b23ff79abccccf7aa6f583b7c43ea9f1aca5e733b2adb68ff17e93eb8b97cf528ff186a4c76ff5bfac83d280f6f0e185e66fedb4beabf83bf489a18cd57afce8ada9eb6390a9aad1fb7b87be8387aa66a2a88e91b769f8878d9bcb45f5eb9da5bb5ef8b0fcb6d94286b5bca9ea59b29f9b8fd837e2a3; JSESSIONID-WYYY=wCKdG^%^2BGQzvG3f^%^2BPoMx44Dj32rvyIk14TsSNd0P38PkmMO7mFG3N2v8DT2UYahdMc4^%^2FNpRgta^%^2BVwsUFiHvIocBP2bSv^%^5Ck2eVxf^%^5ChAajjnM^%^2Bx1JkvapXHx0xCP3JaEXWb2AzyiVjbDrSmNpnzmgJJreF0FDGM^%^5CsbTryUJMnPc01lXvJw^%^5CJ^%^3A1718774310397; playerid=84753085^",
        "origin": "https://music.163.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://music.163.com/",
        "^sec-ch-ua": "^\\^Not/A)Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^126^^, ^\\^Google",
        "sec-ch-ua-mobile": "?0",
        "^sec-ch-ua-platform": "^\\^Windows^^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    song = {
        "ids": f'[{Id}]',
        "level": "standard",
        "encodeType": "aac",
        "csrf_token": "a957962f952014c5ba2fd7c5424424fb"
    }
    music = execjs.compile(open("网易云.js", encoding="utf-8").read()).call("get_data", json.dumps(song))
    Sdata = {
        "params": music.get("encText"),
        "encSecKey": music.get("encSecKey")
    }
    reUrl = "https://music.163.com/weapi/song/enhance/player/url/v1"
    reResponse = requests.post(reUrl, headers=reHeaders, params=Sdata, data=Sdata)
    for j in reResponse.json()['data'][0]:
        items['url'] = reResponse.json()['data'][0]['url']
    print(items)
    lsHeaders = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    filepath = './网易云'
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    try:
        lsResponse = requests.get(items['url'], headers=lsHeaders)
        with open('网易云\\' + items['name'] + '.mp3', 'wb') as f:
            f.write(lsResponse.content)
            print(items['name'] + '.mp3' + '下载成功')
    except Exception as e:
        print('该歌曲需要会员')