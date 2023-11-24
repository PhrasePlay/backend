from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Phrase(models.Model):
    audio_file = models.FileField(upload_to='audios/')
    category = models.ForeignKey(Category, related_name='phrases', on_delete=models.CASCADE)
    caption_en = models.CharField(max_length=255)
    caption_pt = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption_en

class Playlist(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='playlist_covers/')
    phrases = models.ManyToManyField(Phrase, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorited_playlists')
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'playlist') 

    def __str__(self):
        return f"{self.user.username} favorite {self.playlist.name}"