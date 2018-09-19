from django.db import models

class user(models.Model):
    username = models.CharField(max_length=200,primary_key=True)
    pwd = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    time=models.DateTimeField('date published')
    def __str__(self):
        return self.username