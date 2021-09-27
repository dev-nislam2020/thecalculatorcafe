from os import name
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.template.defaultfilters import slugify

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
    slug = models.SlugField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('calculator_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class CalculatorInfo(models.Model):
    calculator = models.ForeignKey(Calculator, on_delete=CASCADE, related_name='caculator_info')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.title is None:
            return self.description[:20]
        return self.title

