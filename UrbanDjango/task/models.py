from django.db import models
#
# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username']

    def __str__(self):
        return self.email

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=9)
    size = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    user = models.ManyToManyField(User, related_name='games')

    def __str__(self):
        return self.title