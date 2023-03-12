from django.urls import path, include
from rest_framework import routers
from .views import UserDataList, UserDataDetail, CategoryViewSet, ExtraViewSet, FoodViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'extras', ExtraViewSet)
router.register(r'foods', FoodViewSet)

urlpatterns = [
    path('users/', UserDataList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDataDetail.as_view(), name='user-detail'),
    path('', include(router.urls)),
]
