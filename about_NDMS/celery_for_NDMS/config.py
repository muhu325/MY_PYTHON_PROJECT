from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'tasks.epon_update',
        # 'schedule': crontab(),#成功
        'schedule': crontab(minute=0, hour=0),
        # 'schedule': crontab(hour=6, minute=33,),
        # 'schedule': timedelta(seconds=5),
        'args': ()
    }
}
