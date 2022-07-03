from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def contacto(request):
    return render(request, "contacto.html")

def experiencia(request):
    return render(request, "experiencia.html")

def proyectos(request):
    return render(request, "proyectos.html")

def social_media(request):
    return render(request, "social_media.html")