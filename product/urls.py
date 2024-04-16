from django.urls import path
from .views import *
urlpatterns=[
    path('products-list/',ProductView.as_view(),name='products'),
    path('categories-list/',CategoriesView.as_view(),name='categories'),
    path('category-list/<int:id>/',CategoryView.as_view(),name='category'),
    path('category-update/<int:id>/',CategoryUpdate.as_view(),name='update'),
    path('product-update/<int:id>/',ProductUpdate.as_view(),name='product_update'),
]