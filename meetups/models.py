from pydoc import describe
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    name=models.CharField(max_length=50, null=True)
    email=models.EmailField(unique=True, null=True)
    user_info=models.TextField(null=True)
    mobile_no=models.CharField(max_length=50, null=True, blank=True)
    birth_day=models.DateField(null=True)
    image=models.ImageField(upload_to='user_image', null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
class Participant(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email

class Speaker(models.Model):
    user= models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200, null=True, blank=True)
    phone=models.CharField(max_length=200, null=True, blank=True)
    meetup_name=models.CharField(max_length=200, null=True, blank=True)
    image=models.ImageField(upload_to='speaker_image')
    bio=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


class Meetup(models.Model):
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    organizer_email=models.EmailField(null=True, max_length=100)
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    participant=models.ManyToManyField(Participant, blank=True)
    meetup_speaker=models.ManyToManyField(Speaker, blank=True)
  
    description=models.TextField()
    image=models.ImageField(upload_to='meetups_images')
    location=models.CharField(max_length=50, null=True)
    location_address=models.TextField()
    activate=models.BooleanField(default=True)
    create=models.DateTimeField(auto_now_add=True)
    meetup_date=models.DateField(null=True)
    from_date=models.DateField(null=True)
    to_date=models.DateField(null=True)
    meetup_time=models.TimeField()
    
    def __str__(self):
        return f'{self.title}'