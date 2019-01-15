import requests, asyncio, json
from bs4 import BeautifulSoup
import aiohttp
import redis


class ProxyPoolGetter(object):

    def __init__(self, number):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', }
        self.base_proxy_getter_url = 'https://www.xicidaili.com/nn/{}'
        assert type(number) == int and int(number) >= 1
        self.number = number + 1

        self.Reids = redis.Redis(host='10.0.0.45', port=6379)

    def _get_proxies_text(self, index):
        r1 = requests.get(self.base_proxy_getter_url.format(index), headers=self.headers)
        assert r1.status_code == 200
        soup = BeautifulSoup(r1.text, 'lxml')
        trs = soup.select('#ip_list  tr')
        return trs, index

    def _parse_proxies_text(self, trs, page_number):
        for i in trs:
            tds = i.select('td')
            try:
                proxy_ip = "%s://%s:%s" % (tds[5].text.strip().lower(), tds[1].text.strip(), tds[2].text.strip())
                proxy_http = tds[5].text.strip().lower()
                address = tds[3].text.strip()
                speed = tds[6].div.attrs['title']
                connect_time = tds[7].div.attrs['title']
                yield proxy_ip, proxy_http, address, speed, connect_time, page_number
            except:
                pass

    async def _test_singl_proxy(self, test_type,proxy, *args, **kwargs):  # 使用aiohttp方式，已经成功
        # print('开始测试',proxy[0])
        url = 'https://www.baidu.com'
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url, proxy=proxy[0], headers=self.headers, timeout=30) as response:
                    if test_type == 1:#传入测试类型用于区分是从网页获取的信息，还是从代理地址池获取的信息
                        assert response.status == 200
                        if proxy[1] == 'http':
                            proxy_info_json = json.dumps([proxy[0], proxy[1], proxy[2], proxy[3], proxy[4], ])
                            tag = self.Reids.sadd('http_set', proxy_info_json)  # 把有效的代理信息转化为json字符串，插入redis中
                            print('插入redis后返回的信息',tag)
                        elif proxy[1] == 'https':
                            pass
                        print("测试成功：代理%s,第%s页" % (proxy[0],proxy[5]))
                    else:
                        if response.status == 200:
                            print("地址池测试成功：代理%s" % (proxy[0]))
                        else:
                            print("地址池测试失败，已从地址池删除：代理%s" % (proxy[0]))
                            proxy_info_json = json.dumps(proxy)
                            self.Reids.srem(http_set,proxy_info_json)

        except Exception as error:
            # print("failed",proxy[0],error)
            pass

    def get_vaild_proxy(self): #从西刺代理获取有效代理并插入reids
        print('准备从西刺代理获取ip')
        try:
            loop = asyncio.get_event_loop()
            tasks = []

            for index in range(1, self.number):
                print(11110)
                trs, page_number = self._get_proxies_text(index)#get请求到西祠代理
                print(11111)
                proxies_info = self._parse_proxies_text(trs, page_number) #解析西祠代理网页，返回包含代理信息的生成器
                print(11112)
                coroutines = [self._test_singl_proxy(1,proxy_info) for proxy_info in proxies_info]#生成测试代理有效性的协程对象list
                print(11113)
                for i in coroutines:
                    tasks.append(asyncio.ensure_future(i))
            print('准备开始时间循环')
            loop.run_until_complete(asyncio.wait(tasks))
        except Exception as error:
            print('Async Error',error)

    def close(self):
        # redis不需要关闭连接？？？？
        pass


    def valid_test(self): #地址池代理有效性检测
        http_set = self.Reids.smembers('http_set')
        try:
            loop = asyncio.get_event_loop()
            tasks = []
            print('正在进行地址池代理测试,共%s个地址'%len(http_set))
            coroutines = [self._test_singl_proxy(2,json.loads(proxy_info)) for proxy_info in http_set]
            for i in coroutines:
                tasks.append(asyncio.ensure_future(i))
            loop.run_until_complete(asyncio.wait(tasks))
        except:
            print('Async Error2')


if __name__ == "__main__":
    obj = ProxyPoolGetter(1)#开启代理池之前，先检查一遍原redis的代理的有效性，然后再获取一次代理，最后开启flask API
    obj.valid_test()#这里进行代理地址池有效性检测
    # obj.get_vaild_proxy()#这里从西刺代理获取有效的代理信息，并放入redis


