from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def Index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)



    return render(request,'index.html',{'posts':posts,'page':page})