import markdown
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from comments.forms import CommentForm
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView


# Create your views here. Very Good
# def index(request):
#     post_list = Post.objects.all()
#     paginator = Paginator(post_list,2)
#     page = request.GET.get('page')

#     try:
#         post_list = paginator.page(page)
#     except PageNotAnInteger:
#         post_list = paginator.page(1)
#     except Emptypage:
#         post_list = paginator.page(paginator.num_pages)

#     return render(request,'blog/index.html',context={
#         'post_list':post_list
#     })

class IndexView(ListView):
    model = Post  # short for queryset = Post.objects.all()
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # 阅读 + 1
#     post.increase_views()
#     # 记得在顶部引入 markdown 模块
#     md = markdown.Markdown(extensions=[
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#         TocExtension(slugify=slugify)
#     ])

#     post.body = md.convert(post.body)
#     form = CommentForm()
#     comment_list = post.comment_set.all()

#     context = {
#         'post':post,
#         'form':form,
#         'toc':md.toc,
#         'comment_list':comment_list
#     }
#     return render(request, 'blog/detail.html', context=context)

class DetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(DetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(DetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          TocExtension(slugify=slugify)
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        # context['form'] = form
        # context['comment_list'] = comment_list
        return context


# def archives(request,year,month):
#     post_list = Post.objects.filter(created_time__year = year,created_time__month = month).order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

class ArchivesView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return Post.objects.filter(created_time__year=year, created_time__month=month)


# def category(request,pk):
#     cate = get_object_or_404(Category,pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request,'blog/index.html',context={'post_list':post_list})

class CategoryView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Post.objects.filter(category=cate)


class TagView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)
