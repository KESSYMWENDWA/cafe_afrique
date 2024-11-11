# AFRIQUE/views.py

from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def style(request):
    return render(request, 'style.html')