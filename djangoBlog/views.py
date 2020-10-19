from django.shortcuts import render

def homepage(request):
    return render(request, 'Home.html')


def aboutpage(request):
    return render(request, 'About.html')

