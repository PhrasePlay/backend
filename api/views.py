from rest_framework import generics
from .models import Phrase
from .serializers import PhraseSerializer

class PhraseListCreate(generics.ListCreateAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
