from django.db import models

class Categoriya(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Products(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    categoriya=models.ForeignKey(Categoriya,on_delete=models.CASCADE,related_name='categoriya')
    discription=models.CharField(max_length=5000,null=True,blank=True)
    image=models.ImageField(upload_to='image',null=True,blank=True)

    def __str__(self):
                return self.name


