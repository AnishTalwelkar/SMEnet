from django.urls import path
from . import views


urlpatterns = [
    #path('', views.home, name='Home-website'),
    path('connect/', views.connect, name='Connect-website'),
    path('', views.about, name='about-website'),
    path('connectrecommendations/', views.connectrecommendations, name='connectrecommendations-website'),
    path('contact/', views.contact, name='contact-website'),
    path('hire/', views.hire, name='hire-website'),
    path('industries/', views.industries, name='industries-website'),
    path('recommend/', views.recommend, name='recommend-website'),
    path('recommendations/', views.recommendations, name='recommendations-website'),
    path('services/', views.services, name='services-website'),
    path('about/index.html', views.home, name='Home-website'),
    path('hire.html', views.hire, name='hire-website'),
    path('connect.html', views.connect, name='Connect-website'),
    path('recommend.html', views.recommend, name='recommend-website'),
    path('contact.html', views.contact, name='contact-website'),
    path('successful/', views.successful, name='successful-website')
]

