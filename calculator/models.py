from os import name
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Calculator(models.Model):
    tag = models.ForeignKey(Tag, on_delete=CASCADE, related_name='caculators')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CalculatorInfo(models.Model):
    calculator = models.ForeignKey(Calculator, on_delete=CASCADE, related_name='caculator_info')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

