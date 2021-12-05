from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm
# from .models import Profile
from django.contrib import messages
from .decorators import unauthenticated, allowed_users

from django.contrib.auth import authenticate, login, logout

# Create your views here.
@unauthenticated
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + username)
            group = Group.objects.get(name='basic')
            user.groups.add(group)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/registration.html', context)

@unauthenticated
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password is incorrect!")
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')


