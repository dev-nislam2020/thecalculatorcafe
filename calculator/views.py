from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Calculator
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    template_name = 'calculator/pages/index.html'
    calculation_list = Calculator.objects.all()
    context = {
        'calculation_list':calculation_list,
    }
    return render(request, template_name, context)

def list(request):
    template_name = 'calculator/pages/calculators.html'
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
    # calculator_template = render_to_string(f'calculator/{calculation_detail.slug}.html')
    calculator_template = f'../{calculation_detail.slug}.html'
    context = {
        'calculation_detail':calculation_detail,
        'calculator_template':calculator_template,
        'tags':tags,
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'calculator/pages/contact.html'
    context = {}
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/')
    else:
        return render(request, template_name, context)

def about(request):
    template_name = 'calculator/pages/about.html'
    context = {
    }
    return render(request, template_name, context)

def privicy(request):
    template_name = 'calculator/pages/privicy.html'
    context = {
    }
    return render(request, template_name, context)

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')