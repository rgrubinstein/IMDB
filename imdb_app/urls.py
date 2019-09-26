from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("movies/", views.movies, name="movies"),
    path("actors/", views.actors, name="actors"),
    path("movies/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("actors/<int:actor_id>/", views.actor_detail, name="actor_detail")
]
