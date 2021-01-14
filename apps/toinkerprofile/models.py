from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToinkerProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	follows =models.ManyToManyField('self',related_name='followed_by',symmetrical=False)#references itself ,symmetrical is set to false because if i follow you,you dont automatically follow me back

User.toinkerprofile=property(lambda u: ToinkerProfile.objects.get_or_create(user=u)[0])# when i signup i dont have to create an oinker profile

