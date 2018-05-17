from itertools import chain
from django.shortcuts import render
from app.models.Copyright import Copyright
from app.models.Post import Post
from django.core.paginator import Paginator

def show_list(request,page=1):
    post_list = Post.objects.order_by('-play_counts')
    paginator = Paginator(post_list,24)
    posts = paginator.page(page)
    for post in posts:
        post.composers = post.get_composers()

    context = {'post_list':posts,
               }
    return render(request, 'post_list.html', context=context)
    # return render(request,'text.html',{'newlist':newlist})


