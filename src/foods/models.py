from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=120)
    SOUPS = 'SOUPS'
    WRAPS = 'WRAPS'
    BURITTOS = 'BURITTOS'
    PANINIS = 'PANINIS'
    BREAKFAST_SANDWHICHES = 'BREAKFAST SANDWHICHES'
    HOT_DRINKS = 'HOT DRINKS'
    GRILLED_CHEESES = 'GRILLED CHEESES'
    CATEGORY_CHOICES = [
        (SOUPS, 'SOUPS'),
        (WRAPS, 'WRAPS'),
        (BURITTOS, 'BURITTOS'),
        (PANINIS, 'PANINIS'),
        (BREAKFAST_SANDWHICHES, 'BREAKFAST SANDWHICHES'),
        (HOT_DRINKS, 'HOT DRINKS'),
        (GRILLED_CHEESES, 'GRILLED CHEESES'),
    ]
    category = models.CharField(
        max_length=150,
        choices=CATEGORY_CHOICES,
        default=SOUPS,
    )
    content = models.TextField()
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.title

