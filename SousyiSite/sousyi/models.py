from django.db import models

class User(models.Model):
    username = models.CharField("Имя", max_length=50)
    email = models.CharField("Почта", max_length=50)
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['Username']
    
    def __str__(self):
        return self.Username

class Artist(models.Model):
    name = models.CharField("Имя исполнителя", max_length=50)
    bio = models.CharField("Описание", max_length=100)
    
    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"
        ordering = ['Name']
    
    def __str__(self):
        return self.Name

class Genre(models.Model):
    name = models.CharField("Название жанра", max_length=50)
    discription = models.TextField("Описание жанра")
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['Name']
    
    def __str__(self):
        return self.Name

class Album(models.Model):
    title = models.CharField("Название Альбома", max_length=50)
    release_date = models.DateField("Дата выхода альбома")
    artist_id = models.ManyToManyField(Artist, verbose_name="Исполнители")
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ['-Release_date', 'Title']
    
    def __str__(self):
        return self.Title

class Track(models.Model):
    title = models.CharField("Название трека", max_length=50)
    duration = models.IntegerField("Длительность (в секундах)")
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist_id = models.ManyToManyField(Artist)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"
        ordering = ['Title']
    
    def __str__(self):
        return self.Title

class Playlist(models.Model):
    title = models.CharField("Название плейлиста", max_length=50)
    created_at = models.DateField("Время создания", auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track)
    
    class Meta:
        verbose_name = "Плейлист"
        verbose_name_plural = "Плейлисты"
        ordering = ['-Created_at', 'Title']
    
    def __str__(self):
        return self.Title