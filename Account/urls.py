from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreate, UserUpdate
from category.views import CategoryViewset
from product.views import ProductViewset
from reklama.views import ReklamaViewset
router = DefaultRouter()
router.register('category', CategoryViewset, basename='category')
router.register('product',ProductViewset,basename='product')
router.register('reklama',ReklamaViewset,basename='reklama')
urlpatterns = [
    path('', include(router.urls)),
    # path('register/', UserCreate.as_view()),
    # path('update/<int:pk>/', UserUpdate.as_view()),

]
