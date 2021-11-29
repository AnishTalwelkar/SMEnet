from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'website/index.html')

def connect(request):
    return render(request, 'website/connect.html')

def about(request):
    return render(request, 'website/about.html')

def connectrecommendations(request):
    return render(request, 'website/connectrecommendations.html')

def contact(request):
    return render(request, 'website/contact.html')

def hire(request):
    return render(request, 'website/hire.html')

def industries(request):
    return render(request, 'website/industries.html')

def recommend(request):
    return render(request, 'website/recommend.html')

def recommendations(request):
    return render(request, 'website/recommendations.html')

def services(request):
    return render(request, 'website/services.html')

def successful(request):
    return render(request, 'website/succesful.html')
