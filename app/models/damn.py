import redis
from django.core.cache import cache
r = redis.Redis()

class Model(object):

    @classmethod
    def get(cls, **kwargs):
        cache_key = '%s_%s' % (cls.__name__, next(iter(kwargs.values())))
        obj = cache.get(cache_key)
        if not obj:
            obj = cls.objects.get(**kwargs)
            cache.set(cache_key,obj)

        return obj
