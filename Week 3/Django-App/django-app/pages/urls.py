# pages/urls.py
from django.urls import path
from . import views
from .views import AboutPageView,  CateringPageView


# MenuPageView,

urlpatterns = [
    path('', views.home, name='home'), 
    path('menu/', views.menu, name='menu'), 
    path('catering/', CateringPageView.as_view(), name='catering'), 
    path('about/', AboutPageView.as_view(), name='about'), 
    # path('contact/', ContactPageView.as_view(), name='contact'), 
    path('contact/', views.contact, name='contact'),
     
]