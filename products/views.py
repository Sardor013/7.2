from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoryGoodsSerializers, GoodSerializers
from .models import Category, Goods
from rest_framework.views import APIView
# Create your views here.

class ListCreateCategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryGoodsSerializers(categories, many=True)
        return Response({'category': serializer.data, 'status': "success"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoryGoodsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'category': serializer.data, 'status': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDestroyCategoryAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoryGoodsSerializers(category)
        return Response({'category': serializer.data, 'status': 'success'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoryGoodsSerializers(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'category': serializer.data, 'status': 'update'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_200_OK)
        serializer = CategoryGoodsSerializers(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'category': serializer.data, 'status': 'updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response({'status': 'delete'}, status=status.HTTP_204_NO_CONTENT)


class ListCreateGoodsAPIView(APIView):
    def get(self, request):
        goods = Goods.objects.all()
        serializer = GoodSerializers(goods, many=True)
        return Response({'goods': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GoodSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'goods': serializer.data, 'status': 'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveUpdateDestroyGoodsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Goods.objects.get(pk=pk)
        except Goods.DoesNotExist:
            return None

    def get(self, request, pk):
        goods = self.get_object(pk)
        if goods is None:
            return Response({'error': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GoodSerializers(goods)
        return Response({'goods': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        goods = self.get_object(pk)
        if goods is None:
            return Response({'error': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GoodSerializers(goods, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'goods': serializer.data, 'status': 'updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        goods = self.get_object(pk)
        if goods is None:
            return Response({'error': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GoodSerializers(goods, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'goods': serializer.data, 'status': 'updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        goods = self.get_object(pk)
        if goods is None:
            return Response({'error': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        goods.delete()
        return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)







