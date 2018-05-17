from django.db import models

from app.models.Composer import Composer
from app.models.Copyright import Copyright

class Post(models.Model):
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
        composers = []
        cr_list = Copyright.objects.filter(pid=self.pid)
        for cr in cr_list:
            composer = Composer.objects.get(cid=cr.cid)
            composer.roles = cr.roles
            composers.append(composer)
        return composers

