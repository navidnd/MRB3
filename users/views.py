from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def users(request):
    return HttpResponse ('Hey bitch--user info')

def register(request):
    form = UserCreationForm()
    return render(request, 'path/path')