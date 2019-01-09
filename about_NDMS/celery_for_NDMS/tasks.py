from celery import Celery
import requests

# app = Celery('tasks', broker='amqp://myuser:mypassword@localhost/myvhost', backend='amqp')
app = Celery('tasks',
             broker='redis://10.0.0.45:6379',
             backend='redis://10.0.0.45:6379')

app.config_from_object('config')


@app.task
def epon_update():
    # response = requests.get("http://www.baidu.com")
    response = requests.get("http://10.0.0.25:8000/epon_create_update")

    # return "已调用定时任务，执行EPON信息更新%s"%response.status_code
    return response.text