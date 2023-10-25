from django.db import models

class Movies(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(max_length=100)
    img=models.ImageField(upload_to='images')


    def __str__(self):
        return self.name