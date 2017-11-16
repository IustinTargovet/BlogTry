from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.list import ListView
from .models import Post

def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3) #3posts on each Page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #If page is out of range deliver lst page results
        posts = paginator.page(paaginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page,
                                                   'posts': posts})

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post,
                                   status  = 'published',
                                   publish__year = year,
                                   publish__month = month,
                                   publish__day = day)
    return render(request, 'blog/post/detail.html', {'post':post})

# Create your views here.
