from django.db import models


# Create your models here.
class UserProfile(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    profile_img = models.ImageField(null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return f"{self.first_name}"
