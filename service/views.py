from django.shortcuts import render
from .models import Services, ServicePricePackage, ServicePriceHeading, ProjectQuotes
from about.models import About
# Create your views here.


def services(request):
    context = {}
    context['service_list']=Services.objects.filter(active=True)
    context['project_quotes']=ProjectQuotes.objects.filter(active=True).last()
    context['about']=About.objects.filter(active=True).last()
    context['s_price_heading']=ServicePriceHeading.objects.filter(active=True).last()
    context['service_prices']=ServicePricePackage.objects.filter(price_category__is_popular=True)
    return render(request, 'services.html', context)