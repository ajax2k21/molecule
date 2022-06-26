from django.db import models

# Create your models here.

class MoleculeApi(models.Model):
    SDF = models.CharField(max_length=100000)
    LSN_Number = models.BigIntegerField()
    Date_Created = models.DateTimeField(auto_now_add=True)

  #  def __str__(self):
   #     return self.Date_Created
        