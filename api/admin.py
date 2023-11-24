from django import forms
from django.contrib import admin
from .models import Phrase, Category, Playlist


class PlaylistAdminForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'
        widgets = {
            'phrases': forms.CheckboxSelectMultiple,
        }

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    form = PlaylistAdminForm

admin.site.register(Phrase)
admin.site.register(Category)
