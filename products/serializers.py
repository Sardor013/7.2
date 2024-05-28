from rest_framework import serializers
from .models import Category, Goods


class CategoryGoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'