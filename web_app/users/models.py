from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Image model 
class Profile(models.Model):
    # Define relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # parameters :Default image when a user doesn't have an image, folder to store images
    image = models.ImageField(default='default.jpg', upload_to='images/')

    def __str__(self):
        return f'{self.user.username} Profile'