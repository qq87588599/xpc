from django.shortcuts import render

from app.models.Comment import Comment
from app.models.Post import Post


# def get_comments(pid):
#     comments_list = Comment.objects.filter(pid=pid).order_by('commentid')



def articleList(request,pid):
    article_list = Post.objects.get(pid=pid)
    article_list.comments = Comment.objects.filter(pid=pid).order_by('commentid')
    article_list.comments_count = article_list.comments.count()
    for comment in article_list.comments:
        if comment.reply != 0:
            comment.replys = Comment.objects.filter(commentid=comment.reply)

    # comments_list = Comment.objects.filter(pid=pid).order_by('commentid')
    # for article in article_list:
    #     article.comments = Comment.objects.filter(pid=article).order_by('commentid')
    context= {"article_list":article_list,
              }
    return render(request,'production.html',context=context)
