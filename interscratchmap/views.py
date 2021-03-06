from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import NameForm
from django.http import HttpResponseRedirect


# to uncomment annotation when signup will done
# @login_required
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'authorization/signup.html', {'form': form})


def login(request):
    return render(request, 'authorization/login.html')


def contact_form(request):

    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():

            return HttpResponseRedirect('/index/')

    else:
        form = NameForm()

    return render(request, 'other/contact_form.html', {'form': form})
