from django.shortcuts import render  # <-- Renders a Django template
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return render(request, "hello.html", {"name": "Nick"})
