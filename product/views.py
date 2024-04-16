from django.shortcuts import render,get_object_or_404
from .serializer import AllProductSerializer,CategoriyaSerilizerView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products,Categoriya
# categoriyalar uchun api
class CategoriesView(APIView):
    def get(self,request):
        categories=Categoriya.objects.all()
        serializer=CategoriyaSerilizerView(categories,many=True)
        return Response(data=serializer.data)
    
    
    def post(self,request):
        serializer=CategoriyaSerilizerView(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CategoryView(APIView):
    def get(self,request,id):
        category=Categoriya.objects.get(id=id)
        serializer=CategoriyaSerilizerView(category)
        return Response(data=serializer.data)
    
class CategoryUpdate(APIView):
    def put(self,request,id):
        category=Categoriya.objects.get(id=id)
        serializer=CategoriyaSerilizerView(instance=category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        try:

            category=Categoriya.objects.get(id=id)
        except Categoriya.DoesNotExist:
            return Response({"messege":"Bu categorya mavjud emas"})
        category.delete()
        return Response({"messege":"Muvaffaqiyatli O'chirildi"})


#Mahsulotlar uchun api
       
class ProductView(APIView):
    def get(self,request):
        products=Products.objects.all()
        serializer=AllProductSerializer(products,many=True)
        return Response(data=serializer.data)
    
    def post(self,request):
        serializer=AllProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class ProductUpdate(APIView):
    def put(self,request,id):
        product=get_object_or_404(Products,id=id)
        serializer=AllProductSerializer(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,id):
        try:
            product=get_object_or_404(Products,id=id)
        except Products.DoesNotExist():
            return Response({"messege":"Mavjud emas "})

        product.delete()
        return Response({"messege":"Muvaffaqiyatli O'chirildi"})

