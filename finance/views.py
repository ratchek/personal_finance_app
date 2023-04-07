from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse(
        "Hello, world. You're at the finance index.\n Don't mind me, just testing da deployment"
    )
