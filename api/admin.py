from django.contrib import admin
from .models import Phrase, Category, Playlist


admin.site.register(Playlist)
admin.site.register(Phrase)
admin.site.register(Category)
