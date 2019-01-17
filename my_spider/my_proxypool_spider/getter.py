import requests, asyncio, json
from bs4 import BeautifulSoup
import aiohttp
import redis,time


class ProxyPoolGetter(object):

    def __init__(self, number):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', }

        assert type(number) == int and int(number) >= 1
        self.number = number + 1

        self.Reids = redis.Redis(host='10.0.0.45', port=6379)



    async def _test_singl_proxy(self, test_type,proxy, *args, **kwargs):
        # 代理有效性检测，内部分成了1.网页代理信息检测，并放入reids。2.现有的redis代理有效性检测
        # print('开始测试',proxy[0])
        url = 'https://www.baidu.com'
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url, proxy=proxy[0], headers=self.headers, timeout=30) as response:
                    if test_type == 1:#传入测试类型用于区分是从网页获取的信息，还是从代理地址池获取的信息
                        assert response.status == 200
                        if proxy[1] == 'http':
                            proxy_info_json = json.dumps(proxy)
                            tag = self.Reids.sadd('http_set', proxy_info_json)  # 把有效的代理信息转化为json字符串，插入redis中
                            print('插入redis后返回的信息',tag)
                        elif proxy[1] == 'https':
                            pass
                        print("测试成功：代理%s," % (proxy[0]))
                    else:
                        if response.status == 200:
                            proxy_info_json = json.dumps(proxy)
                            self.Reids.sadd('http_set', proxy_info_json)
                            print("地址池测试成功：代理%s" % (proxy[0]))
                        else:
                            print("地址池测试失败，已从地址池删除：代理%s" % (proxy[0]))
                            #redis实际有132个，测试只有50+个成功，但没有一个现实失败，所以那些未显示的是已经时效的代理，连response都没有返回了吧。。。
                            proxy_info_json = json.dumps(proxy)
                            self.Reids.srem('http_set',proxy_info_json)

        except Exception as error:
            # print("failed",proxy[0],error)
            pass

    def get_vaild_proxy(self,ProxyClass): #从代理获取有效代理并插入reids
        print('准备从西刺代理获取ip')
        try:
            loop = asyncio.get_event_loop()
            tasks = []

            for index in range(1, self.number):
                try:
                    # print(index)
                    proxies_info = ProxyClass(index).proxies_info
                    # print(11112,index)
                    coroutines = [self._test_singl_proxy(1,proxy_info) for proxy_info in proxies_info]#生成测试代理有效性的协程对象list
                    # print(11113)
                    for i in coroutines:
                        tasks.append(asyncio.ensure_future(i))
                    # print(11114)
                except Exception as e:
                    print('wrong',e)
            print('准备开始事件循环')
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
            for proxy_info in http_set:
                info = self.Reids.srem('http_set',proxy_info)
                print('已从数据库删除信息',info,proxy_info)
            coroutines = [self._test_singl_proxy(2,json.loads(proxy_info)) for proxy_info in http_set]
            for i in coroutines:
                tasks.append(asyncio.ensure_future(i))
            loop.run_until_complete(asyncio.wait(tasks))
        except:
            print('Async Error2')


class XICIProxy(object):
    def __init__(self,index):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', }
        self.index = index
        self.base_proxy_getter_url = 'https://www.xicidaili.com/nn/{}'

    def _get_proxies_text(self):#从西刺代理获取代理信息（未解析）
        r1 = requests.get(self.base_proxy_getter_url.format(self.index), headers=self.headers)
        assert r1.status_code == 200
        soup = BeautifulSoup(r1.text, 'lxml')
        trs = soup.select('#ip_list  tr')
        return trs

    def _parse_proxies_text(self, trs):#解析从西刺代理获取的代理信息，并返回。这是一个生成器
        for i in trs:
            tds = i.select('td')
            try:
                proxy_ip = "%s://%s:%s" % (tds[5].text.strip().lower(), tds[1].text.strip(), tds[2].text.strip())
                proxy_http = tds[5].text.strip().lower()
                address = tds[3].text.strip()
                # speed = tds[6].div.attrs['title']
                # connect_time = tds[7].div.attrs['title']
                yield proxy_ip, proxy_http, address
            except:
                pass

    @property
    def proxies_info(self): #将该方法属性化，返回一个生成器
        trs = self._get_proxies_text()
        genarator = self._parse_proxies_text(trs)
        return genarator

class KuaiDaiLi(object):
    def __init__(self,index):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Host':'www.kuaidaili.com',
            'Referer':'https://www.kuaidaili.com/free/inha/1/',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cookie':'_ga=GA1.2.1602284448.1539573997; channelid=0; sid=1547112288644600; _gid=GA1.2.544960047.1547600027; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1547112290,1547600029; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1547602782'
        }
        self.index = index
        self.base_proxy_getter_url = 'https://www.kuaidaili.com/free/inha/{}/'

    def _get_proxies_text(self):#从西刺代理获取代理信息（未解析）
        r1 = requests.get(self.base_proxy_getter_url.format(self.index), headers=self.headers)
        time.sleep(2)#第一次碰到过快的访问频率，导致503
        # print('状态码：',r1.status_code)
        # print('文本：',r1.text)
        # print("-------------------------------------------------------------------------------------")
        assert r1.status_code == 200
        soup = BeautifulSoup(r1.text, 'lxml')
        trs = soup.select('#list > table > tbody > tr')
        return trs

    def _parse_proxies_text(self, trs):#解析从西刺代理获取的代理信息，并返回。这是一个生成器
        for i in trs:
            tds = i.select('td')
            try:
                proxy_ip = "%s://%s:%s" % (tds[3].text.strip().lower(), tds[0].text.strip(), tds[1].text.strip())
                proxy_http = tds[3].text.strip().lower()
                address = tds[4].text.strip()
                # print('快代理结果：',proxy_ip,proxy_http,address)
                yield proxy_ip, proxy_http, address
            except:
                pass

    @property
    def proxies_info(self): #将该方法属性化，返回一个生成器
        trs = self._get_proxies_text()
        genarator = self._parse_proxies_text(trs)
        return genarator


if __name__ == "__main__":
    obj = ProxyPoolGetter(2)#开启代理池之前，先检查一遍原redis的代理的有效性，然后再获取一次代理，最后开启flask API
    # obj.valid_test()#这里进行代理地址池有效性检测
    obj.get_vaild_proxy(KuaiDaiLi)#这里从西刺代理获取有效的代理信息，并放入redis

#也可以这样来测试吗？。。
#telnetlib.Telnet(verify_ip, verify_ip_port, timeout=10)