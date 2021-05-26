import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Profile, Post

def print_posts(request):
    posts = list(Post.objects.values())

    return JsonResponse({'posts': posts}, safe=False)
