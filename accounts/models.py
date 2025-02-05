from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profail (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date=models.DateField(null=True)
    phone_number=models.CharField(max_length=15)
    city=models.ForeignKey('City',related_name='user_city',on_delete=models.CASCADE,blank=True, null=True)
    user_img=models.ImageField(upload_to='accounta/profile')

    def __str__(self) :
        return str(self.user)
    

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profail.objects.create(user=instance)


class City (models.Model):
    name=models.CharField(max_length=20)
    def __str__(self) :
        return self.name

