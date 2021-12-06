from django.db import models

# Create your models here.
class Sale(models.Model):
    class_type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.class_type)
