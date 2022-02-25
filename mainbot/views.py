from django.shortcuts import render

# Create your views here.
from .models import Comment, Post, Books
from .forms import CommentForm

messages_list_mz = Post.objects.all()
#books_list_mz = Books.objects.all()
#j = []
names_list = ['name', 'description', 'field', 'language', 'pages', 'author',
              'download_link', 'download', 'image'
              ]
#for x in books_list_mz:
#    print(Books.description)


def all_books(request):
    all_books = Books.objects.all()
    return render(request, "books.html",
    {'all_books': all_books})


def botbooks(request):
    rew = Books.objects.all()
    return render(request, "123.html",
    {'all': rew})


def all_messages(request):
    messages_list = Post.objects.all()
    # for x in messages_list:
    context = {
        'messages_list': messages_list,
    }
    return render(request, "test.html", context)


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,

    }

    return render(request, "blog_detail.html", context)