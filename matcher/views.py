from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SockForm

from .models import Sock


@login_required
def my_socks(request):
    sock_list = Sock.objects.filter(owner=request.user.id)
    context = {
        'sock_list': sock_list,
    }
    return render(request, 'index.html', context)


def add_sock(request):
    if request.method == 'POST':
        form = SockForm(request.POST, request.FILES)
        if form.is_valid():
            new_sock = form.save(commit=False)
            new_sock.owner_id = request.user.id
            new_sock.save()
            return redirect('my_socks')
    else:
        form = SockForm()
    return render(request, 'sock_upload.html', {
        'form': form
    })


def detail(request, sock_id):
    sock = get_object_or_404(Sock, pk=sock_id)
    allsocks = Sock.objects.exclude(pk=sock_id)
    sortedSocks = sorted(allsocks, key=lambda i: sock.distance(i))
    distances = [sock.distance(i) for i in sortedSocks]
    print(distances)
    context = {
        'sock': sock,
        'sortedSocks': sortedSocks,
    }
    return render(request, 'detail.html', context)


def home(request):
    sockCount = Sock.objects.count()
    return render(request, 'home.html', {
        'sockCount': sockCount
    })
