from django.shortcuts import render
from .models import About, Workflow
from MainApp.forms import ContactForm

# Create your views here.

def about(request):
    context={}
    context['forms'] = ContactForm()

    context['about'] = About.objects.filter(active=True).last()
    context['workflow'] = Workflow.objects.filter(active=True)[:4]
    return render(request, 'about_us.html', context)