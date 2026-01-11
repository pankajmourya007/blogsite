from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "blog/home.html", {"posts": posts})

def blog_list(request):
    query = request.GET.get("q")

    post_list = Post.objects.all().order_by('-created_at')

    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, "blog/blog_list.html", {
        "posts": posts,
        "query": query
    })


def about(request):
    return render(request, "blog/about.html")

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # increment views
    Post.objects.filter(id=post.id).update(views=F('views') + 1)
    post.refresh_from_db()

    # HANDLE COMMENT POST
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        body = request.POST.get("body")

        if body:
            Comment.objects.create(
                post=post,
                name=request.user.username,
                body=body
            )
            return redirect("post_detail", slug=post.slug)

    comments = post.comments.order_by("-created_at")

    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = post.likes.filter(user=request.user).exists()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "user_has_liked": user_has_liked,
    })    
    post = get_object_or_404(Post, slug=slug)

    # increment views
    Post.objects.filter(id=post.id).update(views=F('views') + 1)
    post.refresh_from_db()

    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = post.likes.filter(user=request.user).exists()

    comments = post.comments.order_by("-created_at")

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "user_has_liked": user_has_liked,
    })
    post = get_object_or_404(Post, slug=slug)

    # increment views
    Post.objects.filter(id=post.id).update(views=F('views') + 1)
    post.refresh_from_db()

    if request.method == "POST" and request.user.is_authenticated:
        Comment.objects.create(
            post=post,
            name=request.user.username,
            body=request.POST.get("body")
        )
        messages.success(request, "Comment added successfully!")
        return redirect("post_detail", slug=post.slug)

    comments = post.comments.order_by("-created_at")

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments
    })

@login_required
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        like.delete()

    return redirect("post_detail", slug=slug)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.name != request.user.username:
        return redirect("post_detail", slug=comment.post.slug)

    comment.delete()
    return redirect("post_detail", slug=comment.post.slug)

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author != request.user:
        return redirect("post_detail", slug=slug)

    post.delete()
    return redirect("blogs")

"""
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})
"""