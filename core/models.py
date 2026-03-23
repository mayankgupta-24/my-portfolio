from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('core', 'Core'),
        ('db', 'Database'),
        ('tools', 'Tools & Async'),
        ('testing', 'testing'),
    ])
    level = models.CharField(max_length=20, default='Intermediate')

    def __str__(self):
        return self.name