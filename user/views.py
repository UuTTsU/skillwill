from django.shortcuts import render
from .models import Person
from django.http import HttpResponse


def user(request):
    user1 = Person.objects.get(pk=1)
    return HttpResponse(f'{user1.first_name}, {user1.last_name}')
