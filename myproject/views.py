from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def index(request):
    if request.user.user_type == 'admin':
        return render(request, 'Admin/dashboard.html')
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        if request.FILES.get('profile_pic'):
            user.profile_pic = request.FILES['profile_pic']
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    return render(request, 'profile.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if not user.check_password(old_password):
            messages.error(request, 'Old password is incorrect!')
        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match!')
        elif len(new_password) < 6:
            messages.error(request, 'Password must be at least 6 characters!')
        else:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password changed successfully!')
            return redirect('login')
    return redirect('profile')
