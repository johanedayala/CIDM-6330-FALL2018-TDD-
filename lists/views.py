from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from lists.models import Item,Institutions,ProgramEducationalObjectives,StudentOutcome
from django.shortcuts import redirect, render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.

def home_page(request):
    return render(request, 'home.html')
#-----------------INSTITUTIONS -------------------------------------
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
    #return redirect(f'/lists/1/')
    return redirect(f'/lists/{list_.id}/')

def view_inst(request, list_id):
    list_ = Institutions.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

# ------------------------- Personal Educational Objectives-----------------------
def add_peos(request,lists_id):
    add_text= request.POST.get('text_objective',False)
    if(add_text == False):
        list_ = Item.objects.get(id=lists_id)
        return render(request, 'list_peos.html', {'list': list_})
    else:
        ProgramEducationalObjectives.objects.create(institution= Item.objects.get(id=lists_id), objective= add_text)    
        list_ = Item.objects.get(id=lists_id)
        #print('I can see this message in my terminal output!',list_)
        return render(request, 'list_peos.html', {'list': list_})
    
def new_peos(request,lists_id):
    item = Item.objects.get(id=lists_id)
    ProgramEducationalObjectives.objects.create(institution=item,
                                                objective=request.POST['objective'])
    #return render(request, 'list_peos.html')
    return redirect(f'/lists/1/inst/{lists_id.id}/')                                        

def view_peos(request,lists_id):
    item = Item.objects.get(id=lists_id)
    list_ = ProgramEducationalObjectives.objects.filter(institution=item).values()
    return render(request, 'list_peos.html', {'list': list_})

# --------------------------Student outcomes -----------------------------------------
def add_so(request,lists_id):
    item_ = Item.objects.get(id=lists_id)
    StudentOutcome.objects.create(institution=item_, studentOutcome='studentOutcome test')
    list_ = StudentOutcome.objects.filter(institution=item_)
    
    return render(request, 'list_so.html', {'list': list_})

def new_so(request):
    item = Item.objects.get(id=1)
    StudentOutcome.objects.create(institution=item,
                                   studentOutcome=request.POST['studentOutcome'])
    return render(request, 'list_so.html')                                            

def view_so(request):
    item = Item.objects.get(id=1)
    list_ = StudentOutcome.objects.get(institution=item)
    return render(request, 'list_so.html', {'list': list_})