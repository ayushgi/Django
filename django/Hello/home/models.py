from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    opinion=models.TextField(max_length=12)
    date=models.DateField()
    def __str__(self):
        return self.name
        return self.email
    


        