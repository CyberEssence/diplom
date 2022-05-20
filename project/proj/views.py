from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
#from .forms import CommentForm
from .models import Post, Category, Video
from django.views.generic import View
from django.urls import reverse_lazy
from .funcs import get_text

# Create your views here.
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    #form = CommentForm()

    return render(request, 'proj/detail.html', {'post': post})

def category(request):
    video = Video.objects.all()
    return render(request, 'proj/video.html', {"video": video})



def search(request):
    query = request.GET.get('query', '')

    #posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    video = Video.objects.filter(Q(caption__icontains=query))
    #video = Video.objects.all()
    return render(request, 'proj/search.html', {'query': query, "video": video})


def video(request):
    video = Video.objects.all()
    return render(request, 'proj/video.html', {"video": video})    