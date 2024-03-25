from django.shortcuts import render
from django.http import HttpResponse
import datetime


def calendar(request):
    return HttpResponse(f'today is {datetime.datetime.now()}')
