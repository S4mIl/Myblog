from django.db import models
from flask_sqlalchemy import Model


class Contact(models.Model):
    name=models.CharField(max_length=20)
    mail=models.EmailField(max_length=200)
    subject=models.CharField(max_length=20)
    message=models.TextField(max_length=500)
    

    def __str__(self):
        return self.mail
