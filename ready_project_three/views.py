from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    index_dict = {'title': 'Home Page'}
    return render(request, 'index.html', context=index_dict)
