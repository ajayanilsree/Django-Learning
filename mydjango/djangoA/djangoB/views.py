from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    movie_details = {
        'movies': 
        [
            {
                'title': 'The Godfather',
                'year': 1972,
                'summary': '',
                'success': True,
            },
            {
                'title': 'The Dark Knight',
                'year': 2008,
                'summary': 'Batman faces the Joker in Gotham City',
                'success': False,
            },
            {
                'title': 'Inception',
                'year': 2010,
                # 'summary': 'A thief steals secrets through dream invasion',
                'success': True,
            },
            {
                'title': 'Interstellar',
                'year': 2014,
                'summary': 'Explorers travel through a wormhole in space',
                'success': True,
            },
            {
                'title': 'Parasite',
                'year': 2019,
                'summary': 'A poor family infiltrates a wealthy household',
                'success': True,
            },
            {
                'title': 'Gladiator',
                'year': 2000,
                'summary': 'A Roman general seeks revenge',
                'success': False,
            }
        ]
    }

    return render(request, 'index.html', movie_details)
