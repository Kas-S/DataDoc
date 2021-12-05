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
            return render(request, 'base/basic.html')
    return render(request, 'base/index.html')



def graphs(request):
    return render(request, 'base/file_page.html')