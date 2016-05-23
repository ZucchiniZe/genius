from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Peak
from .forms import PeakForm


def index(request):
    peaks = Peak.objects.filter(private=False).order_by('-pub_date')[:20]
    return render(request, 'peak/index.html', {
        'peaks': peaks,
        'reason': 'Viewing the 20 most recent peaks'
    })


def index_tag(request, tag):
    peaks = Peak.objects.filter(private=False, tags__name__in=[tag]).distinct()
    return render(request, 'peak/index.html', {
        'peaks': peaks,
        'reason': 'Viewing all the peaks tagged {}'.format(tag)
    })


def index_user(request, username):
    peaks = Peak.objects.filter(private=False, user__username__iexact=username)
    return render(request, 'peak/index.html', {
        'peaks': peaks,
        'reason': "Viewing all of {}'s peaks".format(username)
    })


@login_required
def personal_index(request):
    peaks = Peak.objects.filter(user=request.user, private=True)
    return render(request, 'peak/index.html', {
        'peaks': peaks,
        'reason': 'Viewing all of your private peaks'
    })


def detail(request, pk):
    peak = get_object_or_404(Peak, pk=pk)
    if peak.private and (request.user and peak.user != request.user):
        return render(request, 'peak/not-auth.html', status=403)
    return render(request, 'peak/detail.html', {'peak': peak})


@login_required
def edit(request, pk=None):
    if pk:
        peak = get_object_or_404(Peak, pk=pk)
        if peak.user != request.user:
            return render(request, 'peak/not-auth.html', status=403)
    else:
        peak = Peak(user=request.user)

    form = PeakForm(request.POST or None, instance=peak)
    if request.method == 'POST':
        if form.is_valid():
            new_peak = form.save()
            return HttpResponseRedirect(reverse('peak:detail', kwargs={'pk': new_peak.pk}))

    return render(request, 'peak/create.html', {'form': form})


@login_required
def delete(request, pk):
    peak = Peak.objects.get(pk=pk)
    if request.user == peak.user:
        peak.delete()
        return HttpResponseRedirect(reverse('peak:index'))
    else:
        return render(request, 'peak/not-auth.html', status=403)
