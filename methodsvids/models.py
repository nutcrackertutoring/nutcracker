from django.db import models

class methods(models.Model):
    class Meta:
        permissions = (
        	("view_methods", "Can view methods"),
        )


# Create your models here.
