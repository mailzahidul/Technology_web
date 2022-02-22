from MainApp.models import CompanyInfo, Testimonial, TestimonialHeading, Client, BrandHeading
from blog.models import Blog, BlogHeading
from service.models import Services
from projects.models import ProjectHeading
from about.models import Experience, ProjectStatistics


def context_processor(request):
    context={}
    context['company'] = CompanyInfo.objects.filter(active=True).last()
    context['testimonial'] = Testimonial.objects.filter(active=True)
    context['testimonial_heading'] = TestimonialHeading.objects.filter(active=True).last()

    context['client'] = Client.objects.exclude(company_logo='', active=True)
    context['brandheading'] = BrandHeading.objects.filter(active=True).last()

    context['last_3_blog'] = Blog.objects.filter(active=True)[:3]
    context['blog_heading'] = BlogHeading.objects.filter(active=True).last()

    context['experiences'] = Experience.objects.filter(active=True).last()
    context['project_statistics'] = ProjectStatistics.objects.filter(active=True)
    context['services'] = Services.objects.exclude(bg_image='')[:4]

    context['project_heading'] = ProjectHeading.objects.filter(active=True).last()


    return context