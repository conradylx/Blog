from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Post, Tags, Author, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import CommentsForm


def search(request):
    all_posts = Post.objects.all()
    query = request.GET.get('q')

    latest = Post.objects.order_by('-timestamp')[0:4]
    all_tags = Tags.objects.all()[0:10]
    author = Author.objects.all()

    if query:
        all_posts = all_posts.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': all_posts,
        "latest": latest,
        "all_tags": all_tags,
        "author": author,
    }
    return render(request, "search.html", context)


def contact(request):
    all_posts = Post.objects.all()
    query = request.GET.get('q')

    latest = Post.objects.order_by('-timestamp')[0:4]
    all_tags = Tags.objects.all()[0:10]
    author = Author.objects.all()

    if query:
        all_posts = all_posts.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': all_posts,
        "latest": latest,
        "all_tags": all_tags,
        "author": author,
    }
    return render(request, "contact.html", context)


def index(request):
    queryset = Post.objects.all().order_by('-timestamp')
    latest = Post.objects.order_by('-timestamp')[0:4]
    all_tags = Tags.objects.all()[0:10]
    author = Author.objects.all()
    paginator = Paginator(queryset, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginator_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)
    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages)

    context = {
        "paginator_queryset": paginator_queryset,
        "latest": latest,
        "all_tags": all_tags,
        "author": author,
        "page_request_var": page_request_var,
    }
    return render(request, 'index.html', context)


def post(request, id):
    # all_tags = Tags.objects.all()[0:10]
    posts = get_object_or_404(Post, id=id)
    form = CommentsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.post = posts
            form.save()

    context = {
        # "all_tags": all_tags,
        "post": posts,
        "form": form
    }
    return render(request, 'post.html', context)


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(categories__title=self.kwargs['category'])
        }
        return content


class TagsListView(ListView):
    template_name = 'tags.html'
    context_object_name = 'taglist'

    def get_queryset(self):
        all_tags = Tags.objects.all()[0:10]
        content = {
            'posts': Post.objects.filter(tags__title=self.kwargs['tag']),
            'tags': all_tags,
        }
        return content


def category_list(request):
    categoryList = Category.objects.all()
    latest = Post.objects.order_by('-timestamp')[0:4]
    author = Author.objects.all()

    context = {
        "category_list": categoryList,
        "latest": latest,
        "author": author,
    }
    return context
