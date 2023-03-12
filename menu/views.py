from rest_framework import generics, viewsets
from menu.models import UserData, Category, Extra, Food
from .serializers import CategorySerializer, UserDataSerializer, ExtraSerializer, FoodSerializer
from rest_framework.filters import SearchFilter


class UserDataList(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class UserDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
