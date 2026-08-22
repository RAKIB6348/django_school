from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.user.user_type == 'admin':
        return render(request, 'Admin/dashboard.html')
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


@login_required
def profile(request):
    return render(request, 'profile.html')
