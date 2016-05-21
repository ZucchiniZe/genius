from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import TIL
from .forms import TilForm


def index(request):
    tils = TIL.objects.filter(private=False)[:20]
    return render(request, 'til/index.html', {'tils': tils})


def index_tag(request, tag):
    tils = TIL.objects.filter(private=False, tags__name__in=[tag]).distinct()
    return render(request, 'til/index.html', {'tils': tils})


def index_user(request, username):
    tils = TIL.objects.filter(private=False, user__username__iexact=username)
    return render(request, 'til/index.html', {'tils': tils})


@login_required
def personal_index(request):
    tils = TIL.objects.filter(user=request.user, private=True)
    return render(request, 'til/index.html', {'tils': tils})


def detail(request, pk):
    til = get_object_or_404(TIL, pk=pk)
    return render(request, 'til/detail.html', {'til': til})


@login_required
def edit(request, pk=None):
    if pk:
        til = get_object_or_404(TIL, pk=pk)
        if til.user != request.user:
            return HttpResponseForbidden()
    else:
        til = TIL(user=request.user)

    form = TilForm(request.POST or None, instance=til)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('til:index'))

    return render(request, 'til/create.html', {'form': form})


@login_required
def delete(request, pk):
    til = TIL.objects.get(pk=pk)
    if request.user == til.user:
        til.delete()
        return HttpResponseRedirect(reverse('til:index'))
    else:
        return HttpResponseForbidden()
