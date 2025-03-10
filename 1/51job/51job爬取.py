import requests
import time
import execjs
import pandas as pd
import sys


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "From-Domain": "51job_web",
    "Pragma": "no-cache",
    "Referer": "https://we.51job.com/pc/search?jobArea=000000&keyword=%E7%88%AC%E8%99%AB&searchType=2&keywordType=",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "account-id": "",
    "partner": "",
    "property": "%7B%22partner%22%3A%22%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D000000%26keyword%3D%25E7%2588%25AC%25E8%2599%25AB%26searchType%3D2%26keywordType%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%2C%22keywordType%22%3A%22%22%7D",
    "sec-ch-ua": "Google Chrome",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "user-token": "",
    "uuid": "7a4ac09bd38c8e8c576baf2f8f26977b"
}
url = "https://we.51job.com/api/job/search-pc"

List = []
searchKeywords = ['python', 'javascript', 'C', 'java', 'php', 'c++', 'c#', 'go', 'ruby', 'rust', 'swift', 'kotlin', 'scala', 'visualbasic', 'pascal', 'Fortran', 'perl', 'lua', 'objectivec', 'objectivec++']
for j in range(0, len(searchKeywords)):
    for page in range(1, 50):
        params = {
            "api_key": "51job",
            "timestamp": str(int(time.time())),
            "keyword": searchKeywords[j],
            "searchType": "2",
            "function": "",
            "industry": "",
            "jobArea": "000000",
            "jobArea2": "",
            "landmark": "",
            "metro": "",
            "salary": "",
            "workYear": "",
            "degree": "",
            "companyType": "",
            "companySize": "",
            "jobType": "",
            "issueDate": "",
            "sortType": "0",
            "pageNum": page,
            "requestId": "d36b73d844e2190fc0f00923b54c7781",
            "pageSize": "20",
            "source": "1",
            "accountId": "",
            "pageCode": "sou|sou|soulb"
        }
        cookies = {
            "guid": "5a981d5b48aa3b61a9ae661dff203cf1",
            "nsearch": "jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D",
            "ps": "needv%3D0",
            "partner": "sem_pcbaidupz_2",
            "51job": "cuid%3D247500379%26%7C%26cusername%3DLxXFgjmhhMj7Jw0RRKZuRbx2nw4k2h0uEV3NtbeVsB8%253D%26%7C%26cpassword%3D%26%7C%26cname%3DAYPHahg%252BXA6Xdp04TQC2lg%253D%253D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0xALtQ6UM9uM%26%7C%26cconfirmkey%3D%25241%2524Cs2mbhE.%2524L5o.HrFLVy7TNdNv95SNq.%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D%25241%2524oJWkmAfC%2524LwN81ez1SdPEpfqSC.IYV%252F%26%7C%26to%3Dc97de29e7fc2e072a73e04ab1cf1e3016672ab1e%26%7C%26",
            "sensor": "createDate%3D2024-06-17%26%7C%26identityType%3D2",
            "slife": "lastvisit%3D020000%26%7C%26lowbrowser%3Dnot%26%7C%26lastlogindate%3D20240619%26%7C%26securetime%3DAj5SZlYxB2sHYgM0CTINb1tsVmQ%253D",
            "Hm_lvt_1370a11171bd6f2d9b1fe98951541941": "1716873829,1718611472,1718622570,1718802589",
            "Hm_lpvt_1370a11171bd6f2d9b1fe98951541941": "1718805557",
            "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22247500379%22%2C%22first_id%22%3A%2218fbda795b81121-0acae759203cae8-26001c51-1638720-18fbda795b91570%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmYmRhNzk1YjgxMTIxLTBhY2FlNzU5MjAzY2FlOC0yNjAwMWM1MS0xNjM4NzIwLTE4ZmJkYTc5NWI5MTU3MCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjI0NzUwMDM3OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22247500379%22%7D%2C%22%24device_id%22%3A%2218fbda795b81121-0acae759203cae8-26001c51-1638720-18fbda795b91570%22%7D",
            "acw_sc__v2": "6672e7da1a42e5bb057f95e8f3ef468f41802bb2",
            "search": "jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAPython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%BC%C6%CB%E3%BB%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAobjectivec%2B%2B%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAobjectivec%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAFortran%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21",
            "acw_tc": "ac11000117188085118032440e0082db069be042c84b6dd9f29cf1f527bf1b",
            "acw_sc__v3": "6672efc6e817792ddbff4e6b771869dd8d732a93",
            "JSESSIONID": "5194339081B9B0CB2E56BA731CDA0E7A",
            "ssxmod_itna2": "mqfhiKYKBKDIjxl4iT3RbDCR6Qo1CBCcjjDn9o2WqG=Dl==pxjbM0D140Q6eqoz1GFq12nOC74+XDnRRIeA1A2evMAZn7uoey9akiUzPy6BhLOHF9kwnPPwPUTukpkvlklukz51VlDmXMCLEhKnLVtmoxykLPaj=Zekr3TWX4LnoYyeodd3ud=WRrHLT/nWdWZnEpFZc5qnc6IcbT5P9VI608kaFrycH7PkF1VZQhv3O+xF=8YBp+4u3iEOGAu8AQzO910UYfu9KUZ3CioXYXh8=Xp9nfyUHE5SSfhzz1iLS9P5If681SYzzOG0xGYgzmgGGqkd237h1sTO1q13qtKEHPMeD7jsCDAxx8jGUjG1YPN4b594jjGatP4jqDjKDeu=UA4Ww5aEPAoxlAP4D",
            "ssxmod_itna": "Yqfx9D2QDtqiqxQq0d58+DyGFdDQdKtDgBBQGhx0542eGzDAxn40iDt==Ml==BaDWKaelirwvhwQBrPmhOKhiaTNEDCPGnDBFeWVIDYAkDt4DTD34DYDigKDLDmeD++5KDdfhTyU8RD3qDwDB=DmqG2/T=Dm4DfDDdcC0qIWuQD4qDBDGUxunNDG4Gf8uqD0uwWx8xnlDGWWkUj3lXqyQ+giDxcD0tDIqGXYD7NWduG59wlIqH11aPRKCiDtqD9WQU6teDH8kXS4uasCip5I03KIGDF+GwbQbeQexxq/7mpW5hYbpqGb2fdBxxD=",
            "tfstk": "fnwxO_ATwabm4Ifgho1ujutAJ1suD-E4irrBIV0D1zU8Ayh6GjNgWf387qcmhA0Tylad0cb4InPz-k90nskMBxkZCwbhK9m00Ak_D26Qbqr74c_UDLV80okw4VG_U_r26lKsQ-M_5YMSAmHscI912YitjA9j1KOWP4osCVaslUZSjmisfVGsNAuWMVRZ5dFT2dSSie3HCdw5Qj3LcCv6C8nxMRZjy7VuemhxRbqfocybrlw03b7pRAru9PF_76ArHlNjhDqVHLHQc72tqRjM6qa4euwSwHvnBSaY1XPRLBlj6qF7hbK6CukTNXNTkZdqlS4-T0GWX9ou-4Z4h7IwPoankxiSZ9sLVfNu3XycPKHQToD01P5HaxE_GYIPcJ2KNhYnJcAf2gdw_jio7MEIq6MGxWm--gqk_CllO03h2gdw_jir22jorCRZZ61.."
        }
        try:
            response = requests.get(url, headers=headers, params=params, cookies=cookies)
            path = '/open/noauth/hr/card/18422847' + '?' 'api_key=51job&' + f'timestamp={params["timestamp"]}&' + 'schemeFrom=pc_searchhr_app&jobId=141750888'

            sign = execjs.compile(open('51job逆向.js', encoding='utf-8').read()).call('run', path)
            headers['sign'] = sign
            response.encoding = 'utf-8'

            for i in response.json()['resultbody']['job']['items']:
                items = {
                    "职位名称": i['jobName'],
                    "职位网址": i['jobHref'],
                    "所在区域": i['jobAreaString'],
                    "公司名称": i['companyName'],
                    "学历要求": i['degreeString'],
                    "企业性质": i['companyTypeString'],
                    "所属行业": i['companyIndustryType1Str'],
                    "薪水": i['provideSalaryString'],
                    "工作经验": i['workYearString'],
                    "发布日期": i['issueDateString'],
                    "员工福利": i['jobTags'],
                    "岗位描述": i['jobDescribe']
                }
                print(items)
                List.append(items)
        except Exception as e:
            df = pd.DataFrame(List)
            df.to_excel('51job.xlsx', index=False)
            print('cookies需更新')
            sys.exit()
