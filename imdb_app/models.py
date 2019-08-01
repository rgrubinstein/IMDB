from django.db import models

GENRE_CHOICES = [('drama', 'drama'), ('horror', 'horror')]


# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    birthdate = models.DateTimeField()
    movies = models.ManyToManyField("imdb_app.Movie")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES)

    def __str__(self):
        return self.title
