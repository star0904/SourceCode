import time
import json
import random
import requests
import threading
from queue import Queue
from threading import Lock


class WeiBo(object):
    def __init__(self):
        self.headers = {
            "referer": "https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }
        self.cookies = {
            "SUB": "_2AkMQmn2Hf8NxqwFRmfAUym7qbIp1zQjEieKmxoxcJRMxHRl-yT9kqlVctRB6OxpTaEXlDVfDXNpPUyXTj_5XbtdC13ut"
        }
        self.url = "https://weibo.com/ajax/feed/hottimeline"

        self.ip_list = []
        self.params_queue = Queue()
        self.lock = Lock()

    def get_ip(self):
        with open('./success_ip.json', 'r', encoding='utf-8') as f:
            data_str = f.read()

        lines = data_str.strip().split('\n')

        for line in lines:
            try:
                ip_dict = json.loads(line.strip())
                self.ip_list.append(ip_dict)
            except json.JSONDecodeError as e:
                print(f"解析失败: {e}")

    def get_params(self):
        for page in range(1, 101):
            params = {
                "refresh": "2",
                "group_id": "102803",
                "containerid": "102803",
                "extparam": "discover|new_feed",
                "max_id": str(page),
                "count": "10"
            }
            self.params_queue.put(params)

    def get_data(self):
        while True:
            params = self.params_queue.get()

            with self.lock:
                if not self.ip_list:
                    print("所有代理都已尝试，请求失败")
                    self.get_ip()

                proxies = random.choice(self.ip_list)

            try:
                response = requests.get(self.url, headers=self.headers, cookies=self.cookies, params=params,
                                        proxies=proxies, timeout=3)
                print(f"使用代理 {proxies} 请求成功，状态码: {response.status_code}")
                print(response.text)
                self.params_queue.task_done()

            except Exception as e:
                print(f"使用代理 {proxies} 请求失败: {e}")
                with self.lock:
                    if proxies in self.ip_list:
                        self.params_queue.task_done()
                        self.ip_list.remove(proxies)
                        self.params_queue.put(params)
                        print(f"移除代理 {proxies}，剩余代理数量: {len(self.ip_list)}")

    def main(self):
        thread_obj_list = []

        t_ip = threading.Thread(target=self.get_ip)
        thread_obj_list.append(t_ip)

        time.sleep(2)

        t_params = threading.Thread(target=self.get_params)
        thread_obj_list.append(t_params)

        for i in range(10):
            t_get_data = threading.Thread(target=self.get_data)
            thread_obj_list.append(t_get_data)

        for thread_obj in thread_obj_list:
            thread_obj.daemon = True
            thread_obj.start()

        time.sleep(4)

        for q in [self.params_queue]:
            q.join()


if __name__ == '__main__':
    weibo = WeiBo()
    weibo.main()
