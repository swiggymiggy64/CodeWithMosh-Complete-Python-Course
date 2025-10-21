from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    # SELECT * FROM movies_movie
    # Movie.objects.all()
    # SELECT * FROM movies_movie WHERE release_year...
    # Movie.objects.filter(release_year=1985)

    movies = Movie.objects.all()
    # output = ", ".join([m.title for m in movies])
    # return HttpResponse(output)

    return render(request, "movies/index.html", {"movies": movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "movies/detail.html", {"movie": movie})
