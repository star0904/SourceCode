import re
import json
# import subprocess
import requests
import execjs


class Qunar(object):
    def __init__(self):
        self.start = "深圳"
        self.end = "重庆"
        self.date = "2026-03-31"
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }

    def get_shirley(self):
        url = "https://flight.qunar.com/site/oneway_list.htm"
        params = {
            "searchDepartureAirport": self.start,
            "searchArrivalAirport": self.end,
            "searchDepartureTime": self.date,
            "nextNDays": "0",
            "startSearch": "true",
            "fromCode": "SZX",
            "toCode": "CKG",
            "from": "flight_dom_search",
            "lowestPrice": "null"
        }
        response = requests.get(url, headers=self.headers, params=params)

        shirley = re.search(r'[0-9a-f]{32}', response.text).group()
        return shirley

    def get_params(self, shirley):
        data = execjs.compile(open("./qunar.js", "r", encoding="utf-8").read()).call("getData", self.start, self.end,
                                                                                   self.date, shirley)
        print(data)
        token = execjs.compile(open("./qunar.js", "r", encoding="utf-8").read()).call("getToken")
        headers = {
            "pre": "1c0dc0c7-7e9a24-1145e586-7583f050-ab56a5751237",
            "referer": "https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E6%B7%B1%E5%9C%B3&searchArrivalAirport=%E9%87%8D%E5%BA%86&searchDepartureTime=2025-09-01&searchArrivalTime=2025-09-09&nextNDays=0&startSearch=true&fromCode=SZX&toCode=CKG&from=flight_dom_search&lowestPrice=null",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        }
        headers = {**headers, **token}

        cookies = {
            "QN1": "0000f38030687bbb40d8daa2",
            "QN300": "organic",
            "QN99": "4463",
            "QN601": "a4b87a5fcafe399c504fe1ffe6cbadb7",
            "_i": "VInJOmiMClcwm9v1MRM2L9Jy622q",
            "QN48": "000188802f107bbb40d8ecbd",
            "quinn": "e2728ee4574f1f32a46edd8635cf92f41dd9cab170223479ee2bb7279185733d2380adc18a7a008d374ec6273a487cef",
            "qunar-assist": "{%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}",
            "ariaDefaultTheme": "null",
            "QN57": "17748598915850.3672310533697305",
            "QunarGlobal": "10.80.126.96_10379220_19cb5d1c802_5508|1774859896089",
            "QN58": "1774859891585%7C1774859895529%7C2",
            "QN205": "organic",
            "fid": "152b4a58-b2f4-4e74-a74b-5dcd6b6db1c8",
            "activityClose": "1",
            "QN243": "12",
            "RT": "s=1774859914416&r=https%3A%2F%2Fflight.qunar.com%2F",
            "QN621": "fr%3Dflight_dom_search",
            "Alina": "9ff955c4-74b652-844b9812-86937074-27b769ca368c",
            "QN269": "D9567A002C1311F1896CD2310BB920C2",
            "F235": "1774859919201",
            "ctt_june": "1683616182042##iK3wasPsVhPwawPwas0IW%3DPAVKWIW2DsVPjmaKtNWsaNVPa%3DVKaNW2GIXs28iK3siK3saKg%2BWRtOaRDNVRXOVhPwaUvt",
            "ctf_june": "1683616182042##iK3wVKX%2BVhPwawPwa%3DDwWPaNaSDNVD3AX2POXKvOVPEIas2OXSa%3DESj%3DESvAiK3siK3saKg%2BWRtOaRDNVRX%2BWhPwaUvt",
            "QN25": "4c69d81b-b833-4ab9-ad5c-088a4270bd32-9f992f90",
            "QN42": "%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7",
            "_q": "U.bxqooia7603",
            "_t": "29690443",
            "csrfToken": "3pjrLsdVfldFPz9iOalZvowRkpF9empX",
            "_s": "s_XITZTCSQC3YZ46I6FMFQMD5CZA",
            "_v": "s8ueXDBBif1OkBf0hG1qgHgNuljF_CmvhYon-ZEAN-ORQYTky0-ffVOVA9Uhz3_laleo1WA2gRztZnDk_WqF7g4nRZwlHHR_CksmpQr0yIN-rzcSrSUbVO9ARY-uCCZqY-RYUknK9uZ9Dz7w28dB-c1bFw_5CdfLM8PuEf7abZkT",
            "_vi": "74hWT0Sr8Ia_p2N4WFQvldqUM14T5geNDIGG5bTNZ2cbTZgmnA0cIpExLwN83OGTHvHONrn9NlojpHoBVUkBCGnCQaqi7F22C0bHJ2MjJaf5Lj7yJEHDCyETOKDVNxRFpNaBbskU1Rj-KrKojh9hgexI8SltAtDx5bxon40pwqzM",
            "QN44": "bxqooia7603",
            "cs_june": "33bea9f41607acb2482c812de70249cdd5334145f2b131f5e819ddb87ca6cea736f6f78aaf04b1ddbdcd0120d4d1b31361a668a4da46c07d574a2ef8000b75c9b17c80df7eee7c02a9c1a6a5b97c117964116ecb3f8058e39d376ca0c8c38d1b5a737ae180251ef5be23400b098dd8ca",
            "QN271": "8cf065ea-87ce-403d-bef5-a1eb40a57593",
            "QN668": "51%2C57%2C57%2C54%2C58%2C56%2C50%2C52%2C53%2C52%2C57%2C50%2C57",
            "QN267": "15606262219f878729",
            "11344": "1722403391463##iK3wWRP%2BWwPwawPwa%3DasWR3wWRPsVK0DW23%2BX%3DX8WSv%3DWK3%3DWDfTaPXmVRDAiK3siK3saKg%2BWRtOaR3sVRasVhPwaUvt",
            "11536": "1722403391463##iK3wWRXNWuPwawPwasThWKDOEPj%2BVDiTX23sWSPmaSHTERoRaKWDWS3sVRkRiK3siK3saKg%2BWRtAVK2nWKj%2BawPwaUvt"
        }
        url = "https://flight.qunar.com/touch/api/domestic/wbdflightlist"

        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        print(response.json())
        print(response)

    def main(self):
        shirley = self.get_shirley()
        self.get_params(shirley)


if __name__ == '__main__':
    qunar = Qunar()
    qunar.main()
