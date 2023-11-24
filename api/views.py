from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .models import Phrase, Favorite
from .serializers import UserSerializer, FavoriteSerializer, PhraseSerializer


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

class UserFavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        if self.request.user.id != user_id:
            raise permissions.PermissionDenied('Você não tem permissão para ver esses favoritos.')
        
        return Favorite.objects.filter(user__id=user_id)