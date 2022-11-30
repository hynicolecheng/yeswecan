from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django import forms
from .models import Fridge, Ingredient, Recipe
# Create your views here.

def index(request): #add fridge button, a list of fridges
    fridge_list = Fridge.objects.all() 
    #this will get a comma separated output of non-linked fridge names: 
    #output = ', '.join([q.fridge_name for q in fridge_list])

    template = loader.get_template('fridgelookup/index.html')
    context = {
        'fridge_list': fridge_list
    }
    return render(request, 'fridgelookup/index.html', context)

def results(request, fridge_id): #will show the results (available recipes' urls) for given fridge
    response = "You're looking at the results of fridge %s."
    return HttpResponse(response % fridge_id)

def details(request, fridge_id):#shows fridge contents
    fridge = get_object_or_404(Fridge, pk=fridge_id)
    return render(request, 'fridgelookup/detail.html', {'fridge': fridge})

def update(request, fridge_id):
    response = "You're updating fridge %s."

    


    return HttpResponse(response % fridge_id)