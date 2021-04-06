from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        'posts' : Post.objects.all(),
        'timep' : timezone.now()
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title':"MEEEE"}) 