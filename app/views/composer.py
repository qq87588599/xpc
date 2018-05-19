from itertools import chain
from django.shortcuts import render

from app.helpers.composer_helper import get_posts
from app.models.Composer import Composer


# 将Composer.object.get  替换为 Composer.get 写在对应的model.py中的
# 多重继承的Model中   是为了使用redis优化重复查询.
def oneuser(request,cid):
    composer = Composer.get(cid=cid)
    composer.posts = get_posts(composer.cid,2)
    context = {'composers':composer}
    return render(request,'oneuser.html',context=context)


def userHomePage(request,cid):
    composer = Composer.get(cid=cid)
    composer.posts = get_posts(composer.cid)
    composer.first_post = composer.posts[0]
    composer.else_post = composer.posts[1:]
    context = {
        "composer":composer
    }
    return render(request,'userHomePage.html',context=context)
