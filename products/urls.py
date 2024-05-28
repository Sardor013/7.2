from django.urls import path
from .views import ListCreateGoodsAPIView, RetrieveUpdateDestroyGoodsAPIView, ListCreateCategoryAPIView, RetrieveUpdateDestroyCategoryAPIView

urlpatterns = [
    path('categories/', ListCreateCategoryAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', RetrieveUpdateDestroyCategoryAPIView.as_view(), name='category-detail'),
    path('goods/', ListCreateGoodsAPIView.as_view(), name='goods-list-create'),
    path('goods/<int:pk>/', RetrieveUpdateDestroyGoodsAPIView.as_view(), name='goods-detail'),
]

