import pickle

from django.db import models

import redis
from app.models.damn import Model
from app.models.Composer import Composer
from app.models.Copyright import Copyright

r = redis.Redis()
class Post(models.Model, Model):
    pid = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    thumbnail = models.CharField(max_length=512, blank=True, null=True)
    preview = models.CharField(max_length=512, blank=True, null=True)
    video = models.CharField(max_length=512, blank=True, null=True)
    video_format = models.CharField(max_length=32, blank=True, null=True)
    duration = models.IntegerField()
    category = models.CharField(max_length=512)
    created_at = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    play_counts = models.IntegerField()
    like_counts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'posts'
    def get_composers(self):
        cache_key = 'cr_pid_%s' % self.pid
        composers = [pickle.loads(i) for i in r.lrange(cache_key,0,-1)]
        # 如果redis中没有composers 则从mysql数据库中取
        if not composers:
            cr_list = Copyright.objects.filter(pid=self.pid)
            for cr in cr_list:
                composer = Composer.get(cid=cr.cid)
                composer.roles = cr.roles
                composers.append(composer)
                # 从mysql得到的数据插入进redis
                r.lpush(cache_key,pickle.dumps(composer))
                r.expire(cache_key,60*60)
        return composers

