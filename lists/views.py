from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item,Institutions,programEducationalObjectives,studentOutcome
from django.shortcuts import redirect, render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.

def home_page(request):
    return render(request, 'home.html')
#-----------------INSTITUTIONS -------------------------------------
def view_inst(request, list_id):
    list_ = Institutions.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def new_Inst(request):
    list_ = Institutions.objects.create()
    Item.objects.create(email=request.POST['email'],
                        password=request.POST['password'],
                        confirm_password=request.POST['confirm_password'],
                        name=request.POST['name'],
                        street=request.POST['street'],
                        city=request.POST['city'],
                        state=request.POST['state'],
                        zipcode=request.POST['zipcode'],
                        mission=request.POST['mission'],
                        list=Institutions.objects.get(id=1))
    #return redirect(f'/lists/{list_.id}/')
    return redirect(f'/lists/1/')

def add_inst(request, list_id):
    list_ = Institutions.objects.get(id=list_id)
    Item.objects.create(email=request.POST['email'],
                        password=request.POST['password'],
                        confirm_password=request.POST['confirm_password'],
                        name=request.POST['name'],
                        street=request.POST['street'],
                        city=request.POST['city'],
                        state=request.POST['state'],
                        zipcode=request.POST['zipcode'],
                        mission=request.POST['mission'],
                        list=list_)
    return redirect(f'/lists/1/')
    #return redirect(f'/lists/{list_.id}/')

# ------------------------- Personal Educational Objectives-----------------------
def add_peos(request):
    return render(request, 'add_peos.html')

def new_peos(request):
    list_ = Institutions.objects.get(id=1)
    programEducationalObjectives.objects.create(institution=list_,
                                                objective=request.POST['objective'])
    return render(request, 'add_peos.html')                                            
    #return redirect(f'/lists/post/new')

def view_peos(request):
    list_ = programEducationalObjectives.objects.get(institution=1)
    return render(request, 'list_peos.html', {'list': list_})

# --------------------------Student outcomes -----------------------------------------
def add_so(request):
    return render(request, 'add_so.html')

def new_so(request):
    studentOutcome.objects.create(institution=1,
                                   studentOutcome=request.POST['studentOutcome'])
    return render(request, 'add_so.html')                                            
    #return redirect(f'/lists/post/new')

def view_so(request):
    list_ = programEducationalObjectives.objects.get(institution=1)
    return render(request, 'list_so.html', {'list': list_})