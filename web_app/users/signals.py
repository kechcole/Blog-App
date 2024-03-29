from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# When a user is saved send this signal to create_profile function that 
# acts as a receiver, 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # If model is successfully created create profile object
    if created:
        Profile.objects.create(user=instance)


# save user profile infpor including default image
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Save profile to User database
    instance.profile.save()