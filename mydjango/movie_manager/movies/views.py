from django.shortcuts import render
from . models import MovieInfo
def create(request):
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        summary=request.POST.get('summary')
        movieinfo_obj=MovieInfo(title=title,year=year,summary=summary)
        movieinfo_obj.save()
    return render(request,'create.html')

def list(request):
    # movie_details = {
    #     'movies': 
    #     [
    #         {
    #             'title': 'The Godfather',
    #             'year': 1972,
    #             'summary': 'Based on Mario Puzo',
    #             'success': True,
    #             'img':'godfather.jpg',
    #         },
    #         {
    #             'title': 'The Dark Knight',
    #             'year': 2008,
    #             'summary': 'Batman faces the Joker in Gotham City',
    #             'success': False,
    #             'img':'darkknight.jpg',
    #         },
    #         {
    #             'title': 'Inception',
    #             'year': 2010,
    #             'summary': 'A thief steals secrets through dream invasion',
    #             'success': True,
    #             'img':'inception.jpg',
    #         },
    #         {
    #             'title': 'Interstellar',
    #             'year': 2014,
    #             'summary': 'Explorers travel through a wormhole in space',
    #             'success': True,
    #             'img':'interstellar.jpg',
    #         }
    #     ]
    # }
    movie_details=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_details})

def edit(request):
    return render(request,'edit.html')  

def index(request):
    return render(request,'index.html')