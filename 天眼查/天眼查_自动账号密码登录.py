import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TYC(object):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--ignore-ssl-errors')
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.browser = webdriver.Chrome(options=self.options)

        self.username = input('请输入账号：')
        self.password = input('请输入密码：')
        while True:
            try:
                workbook = openpyxl.load_workbook(input('请输入查询公司文件名：(仅能后缀名为xlsx,xlsm,xltx,xltm文件)'))
                break
            except FileNotFoundError:
                print('文件不存在')
        sheet = workbook['Sheet1']
        self.company = [cell.value for cell in sheet['A']]
        self.browser.get('https://www.tianyancha.com/')
        self.browser.maximize_window()

    def login(self):
        time.sleep(2)
        browser = self.browser
        while True:
            try:
                browser.find_element(By.XPATH, '//*[@id="page-header"]/div/div[2]/div/div[6]/span').click()
                browser.find_element(By.XPATH,
                                     '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[2]').click()
                browser.find_element(By.XPATH,
                                     '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]').click()
                browser.find_element(By.XPATH,
                                     '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[1]/input').send_keys(
                    self.username)
                browser.find_element(By.XPATH,
                                     '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/input').send_keys(
                    self.password)
                browser.find_element(By.XPATH,
                                     '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div[3]/input').click()
                browser.find_element(By.XPATH,
                                     '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/button').click()
                while True:
                    if browser.find_element(By.XPATH, '//*[@id="page-header"]/div/div[2]/div/div[6]').get_attribute(
                            'class') != 'tyc-header-nav-item tyc-nav-user':
                        break
                    else:
                        time.sleep(1)
                break
            except NoSuchElementException:
                print('请手动完成滑块')
                time.sleep(1)

    def get_data(self, company):
        browser = self.browser
        time.sleep(2)
        while True:
            try:
                browser.find_element(By.XPATH,
                                     '//*[@id="page-container"]/div[1]/div/div[3]/div[2]/div[1]/div[1]/input').send_keys(
                    company)
                browser.find_element(By.XPATH,
                                     '//*[@id="page-container"]/div[1]/div/div[3]/div[2]/div[1]/button').click()
                break
            except NoSuchElementException as e:
                print(e)
                time.sleep(1)

        while True:
            try:
                try:
                    try:
                        url = browser.find_element(By.XPATH,
                                                   '//*[@id="page-container"]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[1]/a').get_attribute(
                            'href')
                    except NoSuchElementException as e:
                        url = browser.find_element(By.XPATH,
                                                   '//*[@id="page-container"]/div/div[2]/section/main/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[1]/a').get_attribute(
                            'href')
                except NoSuchElementException:
                    url = browser.find_element(By.XPATH,
                                               '//*[@id="page-container"]/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[1]/a').get_attribute(
                        'href')
                browser.get(url)
                time.sleep(2)
                browser.find_element(By.XPATH,
                                     '//*[@id="page-root"]/div[3]/div/div[3]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div').click()
                while True:
                    if browser.find_element(By.XPATH,
                                            '//*[@id="page-root"]/div[3]/div/div[3]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div').get_attribute(
                        'class') == 'index_export-btn__Jo__h index_disabled__C_xQe':
                        time.sleep(1)
                    else:
                        browser.get('https://www.tianyancha.com/')
                        break
                break
            except NoSuchElementException as e:
                print('请手动完成滑块')
                time.sleep(1)

    def main(self):
        self.login()
        for j in range(0, len(self.company)):
            print('正在查询第{}条数据'.format(j + 1))
            print('正在下载{}数据'.format(self.company[j]))
            self.get_data(self.company[j])
        print('下载完成')
        time.sleep(3)
        self.browser.close()


if __name__ == '__main__':
    tyc = TYC()
    tyc.main()
