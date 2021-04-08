from django.db import models


# Create your models here.
class TodoWork(models.Model):
    title= models.TextField() 
    status=models.CharField(max_length=50)
    today= models.DateField()

    def __str__(self):
        return self.title
    


