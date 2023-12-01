from django.db import models


# Create your models here.
class Music(models.Model):
    name = models.CharField(max_length=20)
    artist = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.name


# create game
    def make_song(name, artist):
        music = Music(name=name, artist=artist)
        music.save()
        return music


    # read all
    def read_all_songs():
        return Music.objects.all()


    # read filtered
    def read_filter(artist):
        return Music.objects.filter(artist=artist)


    # reads by unique identifier(name)
    def read_by_title(name):
        return Music.objects.get(name=name)


    # updates game name
    def update_song(old_song, new_song,old_artist ,new_artist):
        music = Music.objects.get(name=old_song ,artist=old_artist)
        music.name = new_song
        music.artist = new_artist
        music.save()
        return music


    # deletes game
    def delete_music(name):
        Del = Music.objects.filter(name=name)
        Del.delete()
        return Del
