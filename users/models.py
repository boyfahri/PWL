from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField()
    telp = models.CharField(max_length=14)

    def __str__(self):
        return "{} - {}".format(self.user, self.telp)

    class Meta:
        verbose_name_plural = "Biodata"

class API(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "API"
