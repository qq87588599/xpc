from app.models.Copyright import Copyright
from app.models.Post import Post


def get_posts(cid, num=0):
    posts = []
    cr_list = Copyright.objects.filter(cid=cid)
    if len(cr_list) >= num:
        cr_list = cr_list[:num]

    for cr in cr_list:
        posts.append(Post.objects.get(pid=cr.pid))
    return posts