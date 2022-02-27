from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    meetups = [
        { 'title': 'A First Meetup'},
        { 'title': 'A Second Meetup'}
    ]
    return render(request, 'base/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })
