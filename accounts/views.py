from django.shortcuts import render
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


def logout_view(request):
    logout(request)
    return index(request)
