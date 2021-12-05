from django.contrib.auth.models import Group
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.
def index(request):
    if request.user.groups.exists():
        if  request.user.groups.all()[0].name == 'basic':
            if request.method == "POST":
                premium_group = Group.objects.get(name='premium')
                request.user.groups.clear()
                request.user.groups.add(premium_group)
                return redirect('home')
                # user = form.save()
                # username = form.cleaned_data.get('username')
                # messages.success(request, "Account was created for " + username)
                # group = Group.objects.get(name='basic')
                # user.groups.add(group)
            return render(request, 'base/basic.html')
    return render(request, 'base/index.html')

def signup(request): 
    if request.method == 'POST':
        form = forms.AuthForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        form = forms.AuthForm()
    return render(request, 'base/index.html', {'form': form})