from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=64)
    mobile_no = models.IntegerField()
    email = models.EmailField(max_length=32)  #ensures that the given value is in email format

    def __str__(self):
        return f"Name: {self.name}, Mobile_no: {self.mobile_no}, Email: {self.email}"
