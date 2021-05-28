from django.http import JsonResponse

from .models import Post, Comment


def print_posts(request):
    posts = list(Post.objects.values())
    return JsonResponse({'posts': posts})


def open_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post = {'title': post.title, 'description': post.description,
            'content': post.content, 'date': post.date}
    comments = list(Comment.objects.values().filter(post_id=post_id))
    return JsonResponse({'post': post, 'comments': comments})
