from itertools import chain
from django.shortcuts import render

from app.helpers.composer_helper import get_posts
from app.models.Composer import Composer
from app.models.Copyright import Copyright
from app.models.Post import Post
from django.core.paginator import Paginator


def oneuser(request,cid):
    composer = Composer.objects.get(cid=cid)
    composer.posts = get_posts(composer.cid,2)
    context = {'composers':composer}
    return render(request,'oneuser.html',context=context)


def userHomePage(request,cid):
    composer = Composer.objects.get(cid=cid)
    composer.posts = get_posts(composer.cid)
    composer.first_post = composer.posts[0]
    composer.else_post = composer.posts[1:]
    context = {
        "composer":composer
    }
    return render(request,'userHomePage.html',context=context)