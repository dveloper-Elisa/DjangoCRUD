from django.db import models


class Users (models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length = 50)
    telephone = models.BigIntegerField()

    def __str__(self):
        return self.name + ' | '+ str(self.telephone)