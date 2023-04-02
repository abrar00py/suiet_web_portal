from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import NoticeBoard_Engineering,Events,Engineering_Faculty
from django.contrib.auth.decorators import login_required
from account.models import Profile



# Create your views here.
def engineering_homepage(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=user)
        news = NoticeBoard_Engineering.objects.all().order_by('-id')
        Event = Events.objects.all().order_by('-id')[:3]
        context={
            "news":news,
            "event":Event,
            'profile': profile
        }
        
        return render(request, 'engineering/engineering.html', context)
    else:
        return render(request, 'engineering/engineering.html')

@login_required(redirect_field_name='login')
def engineering_event_page(request):
    Event = Events.objects.all().order_by('-id')
    context={
        "event":Event
    }
    return render(request, 'engineering/engineering_allevents.html',context)

@login_required(redirect_field_name='login')
def cs_department(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    context={
        'profile': profile
    }
    if user.groups.filter(name= 'engineering').exists():
        return render(request,'engineering/departments/cs-departments/csdepartment.html',context)
    else:
        return redirect('error')

@login_required(redirect_field_name='login')
def engineering_event_page_details(request,name):
    Event = Events.objects.filter(Title=name)
    context={
        "event":Event
    }
    return render(request, 'engineering/eventsdetails.html',context)

@login_required(redirect_field_name='login')
def cs_department_overview(request):
    user = User.objects.get(username=request.user.username)
    if user.groups.filter(name= 'engineering').exists():
        profile = Profile.objects.get(user=user)
        faculty = Engineering_Faculty.objects.all()
        context = {
            'faculty':faculty,
            'profile': profile
        }
        return render(request, 'engineering/departments/cs-departments/cs_overview.html', context)
    else:
        return redirect('error')

def error(request):
    return render(request,'engineering/error/error.html')


def gallery(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=user)
        Event = Events.objects.all().order_by('-id')[:3]
        context={
            'profile': profile
        }
        
        return render(request,'engineering/engineering_gallery.html',context)
    else:
        return render(request,'engineering/engineering_gallery.html')
    

@login_required(redirect_field_name='login')
def ec_department(request):
    user = User.objects.get(username=request.user.username)
    if user.groups.filter(name= 'engineering').exists():
        return render(request,'engineering/departments/ecdepartment.html')
    else:
        return redirect('error')

@login_required(redirect_field_name='login')
def mech_department(request):
    user = User.objects.get(username=request.user.username)
    if user.groups.filter(name= 'engineering').exists():
        return render(request,'engineering/departments/mechdepartment.html')
    else:
        return redirect('error')

@login_required(redirect_field_name='login')
def civil_department(request):
    user = User.objects.get(username=request.user.username)
    if user.groups.filter(name= 'engineering').exists():
        return render(request,'engineering/departments/civildepartment.html')
    else:
        return redirect('error')

@login_required(redirect_field_name='login')
def aiml_department(request):
    user = User.objects.get(username=request.user.username)
    if user.groups.filter(name= 'engineering').exists():
        return render(request,'engineering/departments/aimldepartment.html')
    else:
        return redirect('error')

def placements(request):
    return render(request,'engineering/placements.html')