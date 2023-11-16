from rest_framework import generics
from .models import Phrase
from .serializers import PhraseSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class PhraseListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer

class PhraseListView(generics.ListAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
    permission_classes = [IsAuthenticated]

class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
