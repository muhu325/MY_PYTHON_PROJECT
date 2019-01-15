from flask import Flask, g
#1. g对象是专门用来保存用户的数据的。
#2. g对象在一次请求中的所有的代码的地方，都是可以使用的。
import redis,json


__all__ = ['app']

app = Flask(__name__)


def get_conn():
    """
    Opens a new redis connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'redis_client'):
        g.redis_client = redis.Redis(host='10.0.0.45', port=6379)
    return g.redis_client


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/get')
def get_proxy():
    """
    Get a proxy
    """
    # print(1111)
    conn = get_conn()
    aaa = conn.srandmember('http_set',1)
    proxy_info = json.loads(aaa[0])
    string = ':'.join(proxy_info)
    return proxy_info[0]


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    """
    conn = get_conn()
    return str(conn.scard('http_set'))


if __name__ == '__main__':
    app.run()
