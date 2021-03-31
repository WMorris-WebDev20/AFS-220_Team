# from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Menu_Item
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class CateringPageView(TemplateView):
    template_name = 'catering.html'

# class MenuPageView(TemplateView):
#     template_name = 'menu.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

def menu(request):

    menu = Menu_Item.objects.all()

    return render(request, "menu.html", {'menu': menu})