from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class DateTimeModel(models.Model):
    # created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        abstract = True

class Blogger(models.Model):
    blogger_fn = models.CharField(max_length=255)
    blogger_mn = models.CharField(max_length=255, null=True, blank=True)
    blogger_ln = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.blogger_fn

    @property
    def name(self):
        blogger_mn = self.blogger_mn
        if not blogger_mn:
            blogger_mn = ''
        return "{} {} {}".format(self.blogger_fn,blogger_mn,self.blogger_ln)

class Category(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.category

    class Meta:
        ordering=['-id']

class Comment(models.Model):
    comment = models.TextField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, default='static/frontend/images/download.jpeg')
    
    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return self.comment

class Post(DateTimeModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name='bloggers')
    comment = models.ManyToManyField(Comment, related_name='comments')
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['-id']

        
    def __str__(self):
        return self.title



    # def save(self, *args, **kwargs):
    #     import re
    #     if self.url:
    #         self.url = re.split(r'href=[\'"]?([^\'" >]+)', self.url)[0]
    #         print(self.url,3333333)
    #     else:
    #         pass
    #     super().save(*args, **kwargs)


