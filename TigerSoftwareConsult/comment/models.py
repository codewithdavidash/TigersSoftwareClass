from django.contrib.auth.models import User
from django.db import models


class HTML(models.Model):
     name = models.CharField(max_length=200)
     video_link = models.CharField(max_length=3000)
     image = models.ImageField(upload_to='core/static/courses_images', default='core/static/mediafiles/html.png')
     date = models.DateTimeField(auto_now_add=True)
     notes = models.FileField(upload_to='core/static/courses_notes', null=True, blank=True)
     def __str__(self):
          return self.name
     class Meta:
          ordering = ('-name',)
          verbose_name_plural = 'HTML'

class CSS(models.Model):
     name = models.CharField(max_length=200)
     video_link = models.CharField(max_length=3000)
     image = models.ImageField(upload_to='core/static/courses_images', default='core/static/mediafiles/css.png')
     date = models.DateTimeField(auto_now_add=True)
     notes = models.FileField(upload_to='core/static/courses_notes', null=True, blank=True)
     def __str__(self):
          return self.name
     class Meta:
          ordering = ('-name',)
          verbose_name_plural = 'CSS'

class JAVASCRIPT(models.Model):
     name = models.CharField(max_length=200)
     video_link = models.CharField(max_length=3000)
     image = models.ImageField(upload_to='core/static/courses_images', default='core/static/mediafiles/javascript.png')
     date = models.DateTimeField(auto_now_add=True)
     notes = models.FileField(upload_to='core/static/courses_notes', null=True, blank=True)
     def __str__(self):
          return self.name
     class Meta:
          ordering = ('-name',)
          verbose_name_plural = 'JAVASCRIPT'

class PYTHON(models.Model):
     name = models.CharField(max_length=200)
     video_link = models.CharField(max_length=3000)
     image = models.ImageField(upload_to='core/static/courses_images', default='core/static/mediafiles/python.png')
     date = models.DateTimeField(auto_now_add=True)
     notes = models.FileField(upload_to='core/static/courses_notes', null=True, blank=True)
     def __str__(self):
          return self.name
     class Meta:
          ordering = ('-name',)
          verbose_name_plural = 'PYTHON'

class HTMLComments(models.Model):
     name = models.CharField(max_length=100)
     comment = models.TextField(max_length=255)
     date = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return self.comment
     class Meta:
          ordering = ('date',)
          verbose_name_plural = 'Students HTML Comments'

class CSSComments(models.Model):
     name = models.CharField(max_length=100)
     comment = models.TextField(max_length=255)
     date = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return self.comment
     class Meta:
          ordering = ('date',)
          verbose_name_plural = 'Students CSS Comments'

class JSComments(models.Model):
     name = models.CharField(max_length=100)
     comment = models.TextField(max_length=255)
     date = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return self.comment
     class Meta:
          ordering = ('date',)
          verbose_name_plural = 'Students JS Comments'

class PythonComments(models.Model):
     name = models.CharField(max_length=100)
     comment = models.TextField(max_length=255)
     date = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return self.comment
     class Meta:
          ordering = ('date',)
          verbose_name_plural = 'Students Python Comments'

