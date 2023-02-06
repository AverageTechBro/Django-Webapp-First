from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from PIL import Image


class HomeWatch(models.Model):
    display = models.ImageField(upload_to='solid/templates')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=225)
    id = models.IntegerField(primary_key=True)


class Blogs(models.Model):
    quote = models.CharField(max_length=150)
    quote_giver = models.CharField(max_length=60)
    title = models.CharField(max_length=225)
    blog_paragraph_main1 = models.TextField(
        validators=[MinLengthValidator(150)], max_length=9999, null=False)
    blog_paragraph_sub1 = models.TextField(max_length=9999, null=True)
    blog_paragraph_main2 = models.TextField(max_length=9999, null=False)
    blog_paragraph_sub2 = models.TextField(max_length=9999, null=True)
    blog_paragraph_sub2II = models.TextField(max_length=9999, null=True)
    blog_paragraph_main3 = models.TextField(max_length=9999, null=False)
    quote_mid_page = models.CharField(max_length=100)
    quote_last_page = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    thumbnail = models.ImageField(upload_to='solid/templates/blog-thumbnail')
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def short_description(self):
        return self.blog_paragraph_main1[:250] + "..."


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=225)
    profile_pic = models.ImageField(upload_to='solid/templates/profile-pic')

    def __str__(self):
        return str(self.user)


class Message(models.Model):
    blogPage = models.ForeignKey(Blogs, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def messages(self):
        return self.__class__.objects.all().order_by('-id')
