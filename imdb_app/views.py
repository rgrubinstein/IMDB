from django.http import HttpResponse
from imdb_app.models import Movie, Actor
from django.shortcuts import render, get_object_or_404
from django.template import loader


# Create your views here.
def homepage(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))


def movies(request):
    template = loader.get_template("movies.html")
    movies = Movie.objects.all()
    return HttpResponse(template.render({"movies": movies}, request))


def actors(request):
    template = loader.get_template("actors.html")
    actors = Actor.objects.all()
    return HttpResponse(template.render({"actors": actors}, request))


def movie_detail(request, movie_id):
    # movie = Movie.objects.get(id=movie_id)
    template = loader.get_template("movie_detail.html")
    movie = get_object_or_404(Movie, pk=movie_id)
    actors = Actor.objects.filter(movies=movie_id)
    return HttpResponse(template.render({"movie": movie, "actors": actors}, request))


def actor_detail(request, actor_id):
    template = loader.get_template("actor_detail.html")
    actor = get_object_or_404(Actor, pk=actor_id)
    movies = Movie.objects.filter(actor=actor_id)
    return HttpResponse(template.render({"actor": actor, "movies": movies}, request))
