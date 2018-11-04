from django.shortcuts import render
from django.http import HttpResponse
from institutions.models import Institutions, Inst
from django.shortcuts import redirect, render
# Create your views here.

def home_page(request):
    return render(request, 'login.html')

def view_list(request, email):
    list_ = Inst.objects.get(id=email)
    return render(request, 'institution.html', {'list': list_})

def new_list(request):
    list_ = Inst.objects.create()
    Institutions.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, email):
    list_ = Inst.objects.get(id=email)
    Institutions.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def post_list(request):
    return render(request, 'institutions/institution.html', {})