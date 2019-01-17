from flask_API import *
from getter import ProxyPoolGetter,XICIProxy,KuaiDaiLi


#简单的代理地址池已完成制作
if __name__ == "__main__":
    proxypool = ProxyPoolGetter(10)
    proxypool.valid_test()
    proxypool.get_vaild_proxy(KuaiDaiLi)
    app.run()