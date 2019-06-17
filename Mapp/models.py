from django.db import models

# Create your models here.
class Mclass1(models.Model):
    name  = models.CharField(max_length = 30)
    age  = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Mclass2(models.Model):
    relation = models.ForeignKey(Mclass1, on_delete = models.CASCADE)
    mage = models.IntegerField()
    maddress = models.TextField()


class teacher(models.Model):
    tname = models.CharField(max_length=50)
    tage = models.IntegerField()
    taddress = models.TextField(max_length=50)

    def __str__(self):
        return self.tname
