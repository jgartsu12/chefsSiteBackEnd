from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=20)
    content = models.TextField()
    description = models.CharField(max_length=120, default="", editable=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return self.title
