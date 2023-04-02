from django.shortcuts import render

# Create your views here.
def webflowcommunity(request):
    return render(request,'webflow-community/index.html')


def sidharth(request):
    return render(request,'webflow-community/sidharthvk.html')

def abrar(request):
    return render(request,'webflow-community/abrar.html')

def aditya(request):
    return render(request,'webflow-community/aditya.html')

def ammar(request):
    return render(request,'webflow-community/ammar.html')

def sathwik(request):
    return render(request,'webflow-community/sathwik.html')

def shraddesh(request):
    return render(request,'webflow-community/shraddesh.html')

def sujay(request):
    return render(request,'webflow-community/sujayad.html')

def sam(request):
    return render(request,'webflow-community/sam.html')

def contact(request):
    return render(request,'webflow-community/contact.html')
