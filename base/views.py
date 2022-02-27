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

def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup!'
        }
    return render(request, 'base/meetup-details.html',{
        'meetup_title': selected_meetup['title'],
        'meetup_descrption': selected_meetup['description']
    })