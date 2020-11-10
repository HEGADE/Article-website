from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class arti(models.Model):
    sno=models.AutoField(primary_key=True)
    content=models.TextField()
    cUser=models.ForeignKey(User,on_delete=models.CASCADE,default='server')
    heading=models.CharField(max_length=200)
    timeStamp=models.DateTimeField(default=now)
    server=models.CharField(default='server', max_length=50)
    somefile=models.FileField()

    datee=models.DateField(default=now)

    def __str__(self):
        return self.heading
