# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, MenuPageView, CateringPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
    path('menu/', MenuPageView.as_view(), name='menu'), 
    path('catering/', CateringPageView.as_view(), name='catering'), 
    path('about/', AboutPageView.as_view(), name='about'), 
    path('contact/', ContactPageView.as_view(), name='contact'), 
     
]