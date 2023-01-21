from django.shortcuts import render

# Create your views here.

def home(request):
    return render('core/home.html')

def about(request):
    return render('core/about.html')

def services(request):
    return render('core/services.html')

def store(request):
    return render('core/store.html')

def contact(request):
    return render('core/contact.html')

def blog(request):
    return render('core/blog.html')

def sample(request):
    return render('core/sample.html')




