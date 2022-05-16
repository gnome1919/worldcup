from django.shortcuts import render

def landing(request):
    return (request, 'landing/landing.html')