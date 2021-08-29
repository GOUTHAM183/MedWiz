from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,upload_to='django_blog/media')
    content = RichTextField(blank=True,null=True)
    
    date_posted = models.DateTimeField(default=timezone.now)
   
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

class Update(models.Model):
    title = title = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,upload_to='django_blog/media')
    content = RichTextField(blank=True,null=True)
    
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("update-detail", kwargs={"pk": self.pk})

class Medicine(models.Model):
    title = title = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,upload_to='django_blog/media')
    content = RichTextField(blank=True,null=True)
    
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("medicine-detail", kwargs={"pk": self.pk})

class Customer(models.Model):
    name = models.CharField(max_length=100)
    from_email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=250)
    symptoms = models.CharField(max_length=250)
    phone = models.IntegerField(max_length=12)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name