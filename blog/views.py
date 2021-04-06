from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView
                                    # DeleteView
)

@login_required
def home(request):
    context = {
        'posts' : Post.objects.all(),
        'timep' : timezone.now()
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    

def about(request):
    return render(request, 'blog/about.html',{'title':"MEEEE"}) 