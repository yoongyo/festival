from django.db import models
from django.conf import settings


class FestivalArea(models.Model):
    name = models.CharField(max_length=50)


class Festival(models.Model):
    name = models.CharField(max_length=50)
    area = models.ForeignKey(FestivalArea, on_delete=models.CASCADE)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tel = models.CharField(max_length=50)
    homepage = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    sponsorship = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    charge = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField()
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)


class FestivalImage(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    image = models.ImageField()


class FestivalComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField()


class FestivalSNS(models.Model):
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)