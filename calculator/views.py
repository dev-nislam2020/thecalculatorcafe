from os import name
from django.shortcuts import render, get_object_or_404
from .models import Calculator, Tag
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    template_name = 'calculator/pages/index.html'
    calculation_list = Calculator.objects.all()
    context = {
        'calculation_list':calculation_list,
    }
    return render(request, template_name, context)

def detail(request, slug):
    template_name = 'calculator/pages/detail.html'
    calculation_detail = get_object_or_404(Calculator, slug=slug)
    tag = calculation_detail.tag
    tags = tag.caculators.all()
    calculator_template = render_to_string(f'calculator/{calculation_detail.slug}.html')
    context = {
        'calculation_detail':calculation_detail,
        'calculator_template':calculator_template,
        'tags':tags,
    }
    return render(request, template_name, context)