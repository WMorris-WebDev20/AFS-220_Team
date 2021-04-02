# from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Menu_Item , Service, ContactData
# Create your views here.

from django import forms
from django.http import HttpResponseRedirect
 

def home(request):

    service = Service.objects.all()
    return render(request, "home.html", {'service':service} )

class CateringPageView(TemplateView):
    template_name = 'catering.html'

# class MenuPageView(TemplateView):
#     template_name = 'menu.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class EditMenuPageView(TemplateView):
    template_name = 'editmenu.html'

def menu(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        menu_data = Menu_Item(name=name, description=description,price=price)

        menu_data.save()
    
        menu = Menu_Item.objects.all()
        
        return render(request, "editmenu.html")
        
    else:
         menu = Menu_Item.objects.all()
         return render(request, "menu.html", {'menu': menu})

    menu = Menu_Item.objects.all()
    return render(request, "menu.html", {'menu': menu} )


class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label='Your Email Address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

def contact(request):
     submitted = False
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_data = ContactData(name=name, email=email,subject=subject,message=message)

        contact_data.save()

        return render(request, 
         'contact.html', {'submitted': True})

        
     else:
         return render(request, 
         'contact.html', {'submitted': False})
 
     return render(request, 
         'contact.html'
       )
