import time
import json
from queue import Queue
import threading
import requests
from lxml import etree


class IpProxy(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }
        self.qy_url = 'https://www.qiyunip.com/freeProxy/{}.html'
        self.zdy_url = 'https://www.zdaye.com/free/{}/'
        self.ip89_url = 'https://www.89ip.cn/index_{}.html'
        self.kdl_url_one = 'http://www.kxdaili.com/dailiip/1/{}.html'
        self.kdl_url_tow = 'http://www.kxdaili.com/dailiip/2/{}.html'
        self.ip3366_url = 'http://www.ip3366.net/free/?stype=1&page={}'

        self.url_queue = Queue()
        self.text_queue = Queue()
        self.test_ip_queue = Queue()

    def get_url(self):
        for page in range(1, 63):
            self.url_queue.put(self.qy_url.format(page))
        for page in range(1, 107):
            self.url_queue.put(self.ip89_url.format(page))
        for page in range(1, 11):
            self.url_queue.put(self.zdy_url.format(page))
            self.url_queue.put(self.kdl_url_one.format(page))
            self.url_queue.put(self.kdl_url_tow.format(page))
        for page in range(1, 8):
            self.url_queue.put(self.ip3366_url.format(page))

    def get_data(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            tree = etree.HTML(response.text)
            if url.find('qiyunip') != -1:
                tr_list = tree.xpath('//*[@id="proxyTable"]/tbody/tr')
                self.text_queue.put(tr_list)
            elif url.find('zdaye') != -1:
                tr_list = tree.xpath('//*[@id="ipc"]/tbody/tr')
                self.text_queue.put(tr_list)
            elif url.find('89ip') != -1:
                tr_list = tree.xpath('//*[@class="layui-table"]/tbody/tr')
                self.text_queue.put(tr_list)
            elif url.find('kxdaili') != -1:
                tr_list = tree.xpath('//*[@class="active"]/tbody/tr')
                self.text_queue.put(tr_list)
            else:
                tr_list = tree.xpath('//*[@id="list"]/table/tbody/tr')
                self.text_queue.put(tr_list)
            self.url_queue.task_done()

    def parse_data(self):
        while True:
            tr_list = self.text_queue.get()
            try:
                for i in tr_list:
                    item = {}
                    item['ip'] = i.xpath('./td[1]/text()')[0].strip()
                    item['port'] = i.xpath('./td[2]/text()')[0].strip()
                    self.test_ip_queue.put(item)
            except IndexError as e:
                for i in tr_list:
                    item = {}
                    item['ip'] = i.xpath('./th[1]/text()')[0].strip()
                    item['port'] = i.xpath('./th[2]/text()')[0].strip()
                    self.test_ip_queue.put(item)
            self.text_queue.task_done()

    def test_ip(self):
        while True:
            result = self.test_ip_queue.get()
            proxies = {
                'http': 'http://' + result['ip'] + ':' + result['port'],
                'https': 'https://' + result['ip'] + ':' + result['port']
            }
            # print(proxies)
            try:
                response = requests.get('http://httpbin.org/ip', headers=self.headers, proxies=proxies, timeout=3)
                response.encoding = 'utf-8'
                if response.status_code == 200:
                    print(response.text)
                    with open('success_ip.json', 'a', encoding='utf-8') as f:
                        f.write(json.dumps(proxies, ensure_ascii=False) + '\n')
                else:
                    print('状态码异常...', response.status_code)
            except Exception as e:
                print('请求超时:')
            self.test_ip_queue.task_done()

    def main(self):
        thread_obj_list = list()

        t_url = threading.Thread(target=self.get_url)
        thread_obj_list.append(t_url)

        for _ in range(50):
            t_get_data = threading.Thread(target=self.get_data)
            thread_obj_list.append(t_get_data)

        t_parse_data = threading.Thread(target=self.parse_data)
        thread_obj_list.append(t_parse_data)

        for _ in range(500):
            t_test_ip = threading.Thread(target=self.test_ip)
            thread_obj_list.append(t_test_ip)

        for t_obj in thread_obj_list:
            t_obj.daemon = True
            t_obj.start()

        time.sleep(4)

        # 当前所有的队列对象中的计数器为零才能解堵塞主程序
        for q in [self.url_queue, self.text_queue, self.test_ip_queue]:
            q.join()


if __name__ == '__main__':
    start_time = time.time()
    ip_proxy = IpProxy()
    ip_proxy.main()
    print('总耗时：', time.time() - start_time)
