from django.db import models

class User(models.Model):
    Username = models.CharField("Имя", max_length=50)
    Email = models.CharField("Почта", max_length=50)

class Playlist(models.Model):
    Title = models.CharField("Название плейлиста", max_length=50)
    Created_at = models.DateField("Время создания", max_length=50)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    Name = models.CharField("Имя исполнителя", max_length=50)
    Bio = models.CharField("Описание", max_length=100)

class Genre(models.Model):
    Name = models.CharField("Название жанра", max_length=50)
    
class Album(models.Model):
    Title = models.CharField("Название Альбома", max_length=50)
    Release_date = models.DateField("Дата выхода альбома")
    Artist_id = models.ManyToManyField(Artist)
    Genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Track(models.Model):
    Title = models.CharField("Название трека", max_length=50)
    Duration = models.IntegerField("Длительность")
    Album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    Plays_count = models.Count
    Likes_count = models.Count
    Playlist_id = models.ManyToManyField(Playlist)