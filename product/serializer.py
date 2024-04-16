from rest_framework import serializers
from .models import Products,Categoriya

class CategoriyaSerilizerView(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta():
        model=Categoriya
        fields=['id','name']
    def validate(self, data):
        name=data.get('name')
        if len(name)<4 or len(name)>50:
            result={
                'messege':"name uzunligi 4 dan uzun 50 dan qisqa bo'lishi kerak"
            }
            raise serializers.ValidationError(result)
        return data

class AllProductSerializer(serializers.ModelSerializer):
    class Meta():
        model=Products
        fields=['id','name','price','categoriya','discription','image']
