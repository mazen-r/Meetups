from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'location': 'NYC',
            'slug': 'A-first-meetup' 
         },
        {
            'title': 'A Second Meetup',
            'location': 'paris',
            'slug': 'A-Second-meetup'
         },
    ]
    return render(request, 'base/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })
