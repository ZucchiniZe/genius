from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'blog/index.html', {'posts': posts})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})


@login_required
def edit(request, pk=None):
    if pk:
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            return HttpResponseForbidden()
    else:
        post = Post(author=request.user)

    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            new_post = form.save()
            return HttpResponseRedirect(reverse('blog:detail', kwargs={'pk': new_post.pk}))

    return render(request, 'blog/create.html', {'form': form})


@login_required
def delete(request, pk):
    post = Postb.objects.get(pk=pk)
    if request.user == post.author:
        post.delete()
        return HttpResponseRedirect(reverse('peak:index'))
    else:
        return HttpResponseForbidden()
