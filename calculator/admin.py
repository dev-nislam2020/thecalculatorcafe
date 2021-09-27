from django.contrib import admin
from .models import Tag, Calculator, CalculatorInfo

# Register your models here.
admin.site.register(Tag)
admin.site.register(Calculator)
admin.site.register(CalculatorInfo)
