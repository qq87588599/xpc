import pickle

from app.helpers.composer_helper import r


class Model(object):

    @classmethod
    def get(cls, **kwargs):
        cache_key = '%s_%s' % (cls.__name__, next(iter(kwargs.values())))
        obj = r.get(cache_key)
        if not obj:
            obj = cls.objects.get(**kwargs)
            r.set(cache_key,pickle.dumps(obj))
        else:
            obj = pickle.loads(obj)
        return obj
