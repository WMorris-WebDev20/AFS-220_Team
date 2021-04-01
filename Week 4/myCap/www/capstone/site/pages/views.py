# from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Menu_Item , Service
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

# class ContactPageView(TemplateView):
#     template_name = 'contact.html'

def menu(request):

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
         form = ContactForm(request.POST)
         if form.is_valid():
             cd = form.cleaned_data
             # assert False
             return HttpResponseRedirect('/contact?submitted=True')
     else:
         form = ContactForm()
         if 'submitted' in request.GET:
             submitted = True
 
     return render(request, 
         'contact.html', 
         {'form': form, 'submitted': submitted}
       )
