from django.db import models
from django.contrib.auth.models import User
from pyparsing import null_debug_action

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null = True)
    first_name = models.CharField(max_length=100, default='', blank=True)
    last_name = models.CharField(max_length=100, default='', blank=True)
    bio = models.TextField(max_length=1000, default='', blank=True)
    branch = models.CharField(max_length=20, default='', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Document(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    document_name = models.CharField(max_length=100)    
    document_uploads = models.FileField(upload_to='document_files')

    def __str__(self):
        return f'{self.user.username}\'s Resume'