# main/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_tenant = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15)
    
    # Adding related_name arguments to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Avoid conflict with auth.User.groups
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Avoid conflict with auth.User.user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    nearby_schools = models.CharField(max_length=255)
    nearby_hospitals = models.CharField(max_length=255)
    no_of_bedrooms = models.IntegerField()
    no_of_bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
