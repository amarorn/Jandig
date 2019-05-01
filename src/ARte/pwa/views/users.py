from ..forms import SignupForm, LoginForm, ExhibitionForm
from ..models import User, Exhibition

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, Http404
from django.db import IntegrityError


def signup(request):
    form = SignupForm(request.POST or None)
    next_url = '/create-exhibition'
    
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        name, email, password = data['name'], data['email'], data['password']
        
        try:
            user = User.objects.create_user(email, password, name=name)
        except IntegrityError as ex:
            form.add_error(None, str(ex))
        else:
            user = auth.authenticate(request, email=user.email, password=password)
            auth.login(request, user)

            return redirect(next_url)
    else:
        form = SignupForm()

    return render(request, 'pwa/signup.jinja2', {'form': form})


def login(request):
    if request.POST:
        pass
    else:
        form = LoginForm()

    return render(request, 'pwa/login.jinja2', {'form': form})


@login_required
def logout(request):
    pass


@login_required
def create_exhibition(request):
    form = ExhibitionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        try:
            exhibition = Exhibition.objects.create(name=data['name'], author=request.user)
        except IntegrityError:
            form.add_error('name', 'This exhibition name already exists')
        else:
            return redirect(f'{request.user.username}/{exhibition.name}/')
    else:
        form = ExhibitionForm()
        return render(request, 'pwa/create-exhibition.jinja2', {'form': form})