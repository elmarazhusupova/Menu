from rest_framework import serializers
from menu.models import UserData, Category, Extra, Food


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
