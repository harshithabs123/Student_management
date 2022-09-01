from django.db import models
# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=50)
    contact_number = models.IntegerField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name