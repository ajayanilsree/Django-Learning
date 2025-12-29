from django.shortcuts import render

def create(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('year'))
        print(request.POST.get('summary'))
    return render(request,'create.html')

def list(request):
    movie_details = {
        'movies': 
        [
            {
                'title': 'The Godfather',
                'year': 1972,
                'summary': 'Based on Mario Puzo',
                'success': True,
                'img':'godfather.jpg',
            },
            {
                'title': 'The Dark Knight',
                'year': 2008,
                'summary': 'Batman faces the Joker in Gotham City',
                'success': False,
                'img':'darkknight.jpg',
            },
            {
                'title': 'Inception',
                'year': 2010,
                'summary': 'A thief steals secrets through dream invasion',
                'success': True,
                'img':'inception.jpg',
            },
            {
                'title': 'Interstellar',
                'year': 2014,
                'summary': 'Explorers travel through a wormhole in space',
                'success': True,
                'img':'interstellar.jpg',
            }
        ]
    }
    return render(request,'list.html',movie_details)

def edit(request):
    return render(request,'edit.html')

def index(request):
    return render(request,'index.html')