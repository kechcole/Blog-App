from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

# Image model 
class Profile(models.Model):
    # Define relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # parameters :Default image when a user doesn't have an image, folder to store images
    image = models.ImageField(default='default.jpg', upload_to='images/')

    def __str__(self):
        return f'{self.user.username} Profile'
    

    # Class method that overides save method.
    def save(self):
        super().save()

        # Call a method from pillow library to open the image
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:    # Check size 
            output_size = (300, 300)    # Specify output size
            img.thumbnail(output_size)  # Resize 
            img.save(self.image.path)   # Save again

        # Else dont touch image