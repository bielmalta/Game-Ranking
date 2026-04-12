from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Conta criada com sucesso. Você já está logado.')
        return redirect('home')

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm(request, data=request.POST or None)
    next_url = request.GET.get('next') or request.POST.get('next') or 'home'

    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        messages.success(request, 'Login realizado com sucesso.')
        return redirect(next_url)

    return render(request, 'accounts/login.html', {
        'form': form,
        'next': next_url,
    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta.')
    return redirect('login')


@login_required
def profile_view(request):
    ratings = request.user.ratings.select_related('game').order_by('-updated_at')
    comments = request.user.comments.select_related('game').order_by('-updated_at')
    return render(request, 'accounts/profile.html', {
        'ratings': ratings,
        'comments': comments,
    })
