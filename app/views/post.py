from _md5 import md5
from itertools import chain


from django.shortcuts import render
from app.models.Copyright import Copyright
from app.models.Post import Post
from django.core.paginator import Paginator
from django.utils.functional import cached_property
from app.helpers.composer_helper import r
# 像引入redis一样引入memcache
from django.core.cache import cache
from django.views.decorators.cache import cache_page


# 根据debug_tool 得知分页查询数量时耗时较长
# 重写查询Paginator里的查询数量方法 并使用redis使用缓存
@cached_property
def count(self):
    sql, params = self.object_list.query.sql_with_params()
    sql = sql % params
    cache_key = md5(sql.encode('utf-8')).hexdigest()
    rows_count = cache.get(cache_key)
    if not rows_count:
        rows_count = self.object_list.count()
        cache.set(cache_key,rows_count,60*60)  # 过期时间
    return int(rows_count)
# 重写Paginator.count方法
Paginator.count = count


# 将排序从play_counts更改为like_counts 查看没有建立索引时不同的载入时间
# 再在mysql中建立like_counts的索引。对比区别
# sql语句的explain语句添加在select前, 好用。

# django自带的memcache 缓存整个view页面  使用@cache_page装饰器即可
# 从django.views.decorators.cache中引入
@cache_page(60*15)
def show_list(request,page=1):
    # order_by优化---建立索引
    post_list = Post.objects.order_by('-play_counts')
    # 查询所有条数,count  使用redis  因为并不会经常更新这个.
    # 属于不敏感信息
    paginator = Paginator(post_list,24)
    posts = paginator.page(page)
    for post in posts:
        post.composers = post.get_composers()

    context = {'post_list':posts,
               }
    return render(request, 'post_list.html', context=context)
    # return render(request,'text.html',{'newlist':newlist})


