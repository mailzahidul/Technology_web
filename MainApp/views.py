from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, HomeBanner, WhyChooseUs, Features
from .forms import ContactForm
from about.models import Workflow, About, TeamMember, TeamHeading
from projects.models import Project

# Create your views here.
def home(request):
    context = {}
    context['workflow'] = Workflow.objects.filter(active=True)[:4]
    context['home_banner'] = HomeBanner.objects.filter(active=True).last()
    context['about'] = About.objects.filter(active=True).last()
    context['project_list'] = Project.objects.filter(active=True, is_published=True)[:10]
    context['why_choose_us'] = WhyChooseUs.objects.filter(active=True).last()
    context['features'] = Features.objects.filter(active=True)
    context['team_member'] = TeamMember.objects.filter(active=True)
    context['team_heading'] = TeamHeading.objects.filter(active=True).last()
    return render(request, 'index.html', context)


def contact_us(request):
    context={}
    context['forms'] = ContactForm()
    return render(request, 'contact.html', context)



def contact_form(request):
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Your message was sent successfully. Thanks.")
        else:
            messages.error(request, forms.errors)
    return redirect(request.META.get('HTTP_REFERER'))