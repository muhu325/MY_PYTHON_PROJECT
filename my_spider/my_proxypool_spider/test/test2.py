import aiohttp,asyncio
async def test_single_proxy(self, proxy):
    """
    text one proxy, if valid, put them to usable_proxies.
    """
    try:
        async with aiohttp.ClientSession() as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('Testing', proxy)
                async with session.get(self.test_api, proxy=real_proxy, timeout=get_proxy_timeout) as response:
                    if response.status == 200:
                        self._conn.put(proxy)
                        print('Valid proxy', proxy)
            except (ProxyConnectionError, TimeoutError, ValueError):
                print('Invalid proxy', proxy)
    except (ServerDisconnectedError, ClientResponseError, ClientConnectorError) as s:
        print(s)
        pass


def test(self):
    print('ValidityTester is working')
    try:
        loop = asyncio.get_event_loop()
        tasks = [self.test_single_proxy(proxy) for proxy in self._raw_proxies]
        loop.run_until_complete(asyncio.wait(tasks))
    except ValueError:
        print('Async Error')