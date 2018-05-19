from django.core.paginator import Paginator
from django.shortcuts import render

from app.models.Comment import Comment
from app.models.Composer import Composer
from app.models.Copyright import Copyright
from app.models.Post import Post


# def get_comments(pid):
#     comments_list = Comment.objects.filter(pid=pid).order_by('commentid')



def articleList(request,pid,page=1):
    article_list = Post.get(pid=pid)
    article_list.comments = Comment.objects.filter(pid=pid).order_by('-commentid')
    article_list.comments_count = article_list.comments.count()
    article_list.creator_lists = Copyright.objects.filter(pid=pid)
    for creator in article_list.creator_lists:
        creator.composer = Composer.get(cid=creator.cid)

    # paginator = Paginator(article_list,10)
    # posts = paginator.page(page)
    for comment in article_list.comments:
        if comment.reply != 0:
            comment.replys = Comment.objects.filter(commentid=comment.reply)


    context= {"article_list":article_list,
              }
    return render(request,'production.html',context=context)


def getComment(request):
    return None