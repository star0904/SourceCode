import time
import random
import redis
import pymongo
import hashlib
import requests
import threading
from queue import Queue
from threading import Lock


class WeiBo(object):
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(host='localhost', port=27017)
        self.collection = self.mongo_client['WeiBo']['data']
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
        self.json_queue = Queue()
        self.content_dict_queue = Queue()
        self.lock = Lock()

        self.redis_client = redis.Redis()

    def get_ip(self):
        url = "https://dps.kdlapi.com/api/getdps/?secret_id=o8qsd4v4sy7zlt5t8h9t&signature=ppq2byj75n805i79wusgwy0vul4zktda&num=24&pt=1&format=json&sep=1"
        response = requests.get(url=url, headers=self.headers)
        for i in response.json()['data']['proxy_list']:
            self.ip_list.append(i)
        print('ip提取成功:', self.ip_list)

    def get_params(self):
        for page in range(1, 10001):
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
                    print("所有代理都已尝试，重新获取ip")
                    self.get_ip()

                result = random.choice(self.ip_list)

            proxies = {
                'http': result,
                'https': result
            }
            # print(proxies)

            try:
                response = requests.get(self.url, headers=self.headers, cookies=self.cookies, params=params,
                                        proxies=proxies, timeout=3)
                if response.status_code == 200:
                    print(f"使用代理 {proxies} 请求成功，状态码: {response.status_code}")
                    # print(response.text)
                    self.json_queue.put(response.json())
                    self.params_queue.task_done()
                else:
                    print(f"使用代理 {proxies} 请求失败，状态码: {response.status_code}")
                    with self.lock:
                        if result in self.ip_list:
                            self.ip_list.remove(result)
                    self.params_queue.task_done()
                    self.params_queue.put(params)

            except Exception as e:
                print(f"使用代理 {proxies} 请求失败: {e}")
                self.params_queue.task_done()
                self.params_queue.put(params)
                with self.lock:
                    if result in self.ip_list:
                        self.ip_list.remove(result)
                        print(f"移除代理 {result}，剩余代理数量: {len(self.ip_list)}")
            time.sleep(random.uniform(0.8, 3))

    def parse_data(self):
        while True:
            json_data = self.json_queue.get()

            for i in json_data["statuses"]:
                item = {}
                item["博主"] = i["user"]["screen_name"]
                item["内容"] = i["text"]
                item["转发量"] = i["reposts_count"]
                item["评论数"] = i["comments_count"]
                item["发表时间"] = i["created_at"]
                self.content_dict_queue.put(item)
            self.json_queue.task_done()

    @staticmethod
    def get_md5(item):
        md5_hash = hashlib.md5(str(item).encode('utf-8')).hexdigest()
        return md5_hash

    def save_data(self):
        while True:
            item_list = []

            for _ in range(50):
                item = self.content_dict_queue.get()
                value = self.get_md5(item)
                result = self.redis_client.sadd('movie:filter', value)

                if result:
                    item_list.append(item)
                else:
                    print('数据重复...')
                self.content_dict_queue.task_done()
            self.collection.insert_many(item_list)
            print('保存成功: {}条数据', format(len(item_list)))

    def main(self):
        self.get_ip()

        thread_obj_list = []

        t_params = threading.Thread(target=self.get_params)
        thread_obj_list.append(t_params)

        for i in range(500):
            t_get_data = threading.Thread(target=self.get_data)
            thread_obj_list.append(t_get_data)

        for i in range(2):
            t_parse_info = threading.Thread(target=self.parse_data)
            thread_obj_list.append(t_parse_info)

        t_save_data = threading.Thread(target=self.save_data)
        thread_obj_list.append(t_save_data)

        for thread_obj in thread_obj_list:
            thread_obj.daemon = True
            thread_obj.start()

        time.sleep(4)

        for q in [self.params_queue]:
            q.join()


if __name__ == '__main__':
    start_time = time.time()
    weibo = WeiBo()
    weibo.main()
    print('总耗时：', time.time() - start_time)
