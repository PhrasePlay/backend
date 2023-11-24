from django.urls import path
from . import views

urlpatterns = [
    path('phrases/', views.PhraseListView.as_view(), name='phrase-list'),
    path('register/', views.CreateUserView.as_view(), name='create-user'),
    path('users/<int:user_id>/favorites/', views.UserFavoriteListView.as_view(), name='user-favorites')
]