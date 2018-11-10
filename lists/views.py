from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item,Institutions
from django.shortcuts import redirect, render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

#def view_list(request, list_id):
    #list_ = Institutions.objects.get(id=list_id)
    #return render(request, 'list.html', {'list': list_})

def view_inst(request, list_id):
    list_ = Institutions.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_Inst(request):
    list_ = Institutions.objects.create()
    #Item.objects.create(text=request.POST['item_text'], list=list_)
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
    return redirect(f'/lists/{list_.id}/')

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
    return redirect(f'/lists/{list_.id}/')
