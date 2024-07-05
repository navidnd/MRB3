from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import baseUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def users(request):
    return HttpResponse ('Hey bitch--user info')

def register(request):

    if request.method == 'POST':
        form = baseUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'SUCCESS!')
            pass

    else :
        form = baseUserForm()
    pass

@login_required
def profilePage(request):
    return HttpResponse('profile page')
