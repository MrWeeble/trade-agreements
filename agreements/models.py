from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    iso_num = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.name, self.iso_num)


class Agreement(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    parties = models.ManyToManyField(to='Country', related_name='agreements')

    def __str__(self):
        return "{} ({})".format(self.name, self.id)

