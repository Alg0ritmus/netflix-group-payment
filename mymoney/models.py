from django.db import models

# Create your models here.
class Vydavky(models.Model):
    name  = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Polozka(models.Model):
    vydavok = models.ForeignKey(Vydavky,on_delete=models.CASCADE)
    suma = models.FloatField(default=0)
    poznamka =  models.CharField(max_length=300)
    pub_date = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.poznamka