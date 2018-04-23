from django.db import models

class physics(models.Model):
    class Meta:
        permissions = (
        	("view_physics", "Can view physics"),
        )

# Create your models here.
