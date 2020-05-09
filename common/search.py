from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

from posts.models import Post


@require_GET
def search_site(request):


    s = request.GET.get('s')
    if s and s != '':
        posts = Post.objects.all()
        users = User.objects.exclude(id=request.user.id)
        posts = posts.filter(
            Q(title__contains=s) |
            Q(description__contains=s)
        ).order_by('-created').distinct()
        users = users.filter(
            Q(username__contains=s) |
            Q(first_name__contains=s) |
            Q(last_name__contains=s)
        ).distinct()
        return render(request, 'search/result.html', {'posts': posts, 'users': users})
    else:
        return redirect('dashboard')


