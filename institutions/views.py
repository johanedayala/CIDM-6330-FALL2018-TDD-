from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from institutions.models import Institutions, Inst
from django.shortcuts import redirect, render
from .models import Inst
from .forms import InstForm
# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
#------------------------------------------------------------------------------
def post_list(request):
    posts = Inst.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'institutions/base.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Inst, pk=pk)
    return render(request, 'institutions/institution_detail.html', {'post': post})

def post_new(request):
    form = InstForm()
    return render(request, 'institutions/institution_edit.html', {'form': form})