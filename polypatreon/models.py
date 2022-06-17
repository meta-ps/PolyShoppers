from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255,null=False,blank=False)
    walletid = models.CharField(max_length=255,null=False,blank=False)
    about = models.CharField(max_length=255,null=True,blank=True)
    youtube=models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.username

