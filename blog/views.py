from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from users.models import Profile
from .forms import PostForm
from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'blog/Home.html', context)


def NewPost(request):
    common_tags = Post.tags.most_common()[:4]
    form = PostForm(request.POST)
    print(form.errors)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            newpost = form.save(commit=False)
            newpost.slug = slugify(newpost.title)
            newpost.save()
            # Without this next line the tags won't be saved.
            form.save_m2m()
            return redirect("post-detail", slug=newpost.slug)
        else:
            messages.error(request, f"{form.errors}")

    context = {
        'common_tags': common_tags,
        'form': form,
    }
    return render(request, 'blog/newPost.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


def get_user_profile(request, username):
    user = User.objects.get(username=username)

    return render(request, 'users/profiles.html', {"p_user": user})

# class PostDetailView(DetailView):
#     model = Post


def detail(request, slug):
    #article = Article.objects.filter(id = id).first()
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    title = post.title
    return render(request, "blog/detail.html", {"post": post, "comments": comments, "title": title})


@login_required(login_url="login")
def deletePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, f"Post '{post.title}' deleted")

    return redirect("blog-home")


@login_required(login_url="login")
def updatePost(request, slug):

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)

        post.author = request.user
        post.save()
        form.save_m2m()

        messages.warning(request, "Your post has been updated")
        return redirect("post-detail", slug=post.slug)

    else:
        messages.error(request, f"{form.errors}")
    return render(request, "blog/update.html", {"form": form, "post": post, })


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'common_tags': common_tags,
        'posts': posts,
    }
    return render(request, 'blog/tags.html', context)


def addComment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print(request.method == "POST")
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content)

        newComment.post = post
        print(newComment.post)

        newComment.save()
    return redirect(reverse("post-detail", kwargs={"slug": slug}))


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # form = PostForm(request.POST)
    fields = ['title', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    title = {'title': 'About'}
    return render(request, 'blog/About.html', title)


def help(request):
    title = {'title': 'Help'}
    return render(request, 'blog/Help.html', title)
