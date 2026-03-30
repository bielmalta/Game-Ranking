from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('game_search')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('game_search')
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('game_search')
    error = None
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user:
            login(request, user)
            return redirect(request.GET.get('next', 'game_search'))
        error = 'Usuário ou senha incorretos.'
    return render(request, 'accounts/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    ratings  = request.user.ratings.select_related('game').order_by('-game__title')
    comments = request.user.comments.select_related('game').order_by('-created_at')
    return render(request, 'accounts/profile.html', {
        'ratings': ratings,
        'comments': comments,
    })