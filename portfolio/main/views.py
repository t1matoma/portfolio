from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'main/home.html')

def contacts(request):
    return render(request, 'main/contacts.html')

