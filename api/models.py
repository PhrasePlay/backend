from django.db import models

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