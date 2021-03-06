from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc = models.TextField()
    def __repr__(self):
        return "dojos: ---,{} ----{}, ----{}, -----{}".format(self.name, self.city, self.state, self.desc)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name = "ninjas")
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    def __repr__(self):
        return "ninjas: ---,{} ----{}, ----{}".format(self.dojo, self.first_name, self.last_name)