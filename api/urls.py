from django.urls import path
from . import views

urlpatterns = [
    path('phrases/', views.PhraseListView.as_view(), name='phrase-list'),
    path('register/', views.CreateUserView.as_view(), name='create-user'),
]