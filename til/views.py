from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
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
def create(request):
    if request.method == 'POST':
        form = TilForm(request.POST)
        if form.is_valid():
            tags = form.cleaned_data.pop('tags')
            form.cleaned_data['user'] = request.user
            til = TIL(**form.cleaned_data)
            til.save()
            til.tags.add(*tags)
            return HttpResponseRedirect(reverse('til:index'))
    else:
        form = TilForm()

    return render(request, 'til/create.html', {'form': form})
