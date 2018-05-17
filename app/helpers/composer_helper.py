from app.models.Copyright import Copyright
from app.models.Post import Post


def get_posts(cid, num=0):
    posts = []
    cr_list = Copyright.objects.filter(cid=cid)
    if len(cr_list) >= num and num != 0 :
        cr_list = cr_list[:num]

    for cr in cr_list:
        post = Post.objects.get(pid=cr.pid)
        post.roles = cr.roles
        posts.append(post)
    return posts