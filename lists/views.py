from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from lists.models import Item,Institutions,programEducationalObjectives,studentOutcome
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
    return redirect(f'/lists/1/')
    #return redirect(f'/lists/{list_.id}/')

def view_inst(request, list_id):
    list_ = Institutions.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

# ------------------------- Personal Educational Objectives-----------------------
def add_peos(request,lists_id):
    #item_ = get_object_or_404(Item, id=id)
    #item_id= 
    item_ = Item.objects.get(id=lists_id)
    programEducationalObjectives.objects.create(institution=item_, objective='test')
    list_ = programEducationalObjectives.objects.filter(institution=item_)
    #return render(request, 'add_peos.html', {'post': item_})
    return render(request, 'list_peos.html', {'list': list_})
    #return redirect(f'/lists/1/ins/{item_.id}')
    #return HttpResponseRedirect(reverse('redirect_peos',args=(item_.id,)))

def redirect_peos(request,id):
    return redirect(f'/lists/1/inst/{id}')


def new_peos(request,id):
    item = Item.objects.get(id=1)
    programEducationalObjectives.objects.create(institution=item,
                                                objective=request.POST['objective'])
    return render(request, 'list_peos.html')                                            
    #return redirect(f'/lists/post/new')

def view_peos(request):
    item = Item.objects.get(id=1)
    list_ = programEducationalObjectives.objects.get(institution=item)
    return render(request, 'list_peos.html', {'list': list_})

# --------------------------Student outcomes -----------------------------------------
def add_so(request,lists_id):
    item_ = Item.objects.get(id=lists_id)
    return render(request, 'list_so.html')

def new_so(request):
    item = Item.objects.get(id=1)
    studentOutcome.objects.create(institution=item,
                                   studentOutcome=request.POST['studentOutcome'])
    return render(request, 'list_so.html')                                            

def view_so(request):
    item = Item.objects.get(id=1)
    list_ = studentOutcome.objects.get(institution=item)
    return render(request, 'list_so.html', {'list': list_})