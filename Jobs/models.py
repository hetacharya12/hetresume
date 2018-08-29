from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    from_date=models.DateField()
    to_date = models.DateField()
    summary = models.TextField()

class Myimage(models.Model):
    image = models.ImageField(upload_to='images/')
