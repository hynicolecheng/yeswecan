from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django import forms
from .forms import FridgeForm2
from .models import Fridge, Recipe
# Create your views here.

def index(request): #add fridge button, a list of fridges
    #fridge_list = Fridge.objects.all() 
    #this will get a comma separated output of non-linked fridge names: 
    #output = ', '.join([q.fridge_name for q in fridge_list])
    fridge_list = Fridge.objects.all() 
    template = loader.get_template('fridgelookup/index.html')
    context = {
        'fridge_list': fridge_list
    }
    return render(request, 'fridgelookup/index.html', context)

def results(request, fridge_id): #will show the results (available recipes' urls) for given fridge
    response = "You're looking at the results of fridge %s."
    return HttpResponse(response % fridge_id)

def detail(request, fridge_id):#shows fridge contents
    fridge = get_object_or_404(Fridge, pk=fridge_id)
    fridge = Fridge.objects.get(pk=1)
    fridge.save()
    context = {
        'fridge': fridge,
        'ingredients': fridge.ingredients.keys()
    }
    return render(request, 'fridgelookup/detail.html', context)

def update(request, fridge_id):
    fridge = get_object_or_404(Fridge, pk=fridge_id)
    """if request.method == 'POST':
        form = FridgeForm2(request.POST)
        if form.is_valid():
            result = form.cleaned_data
            fridge.ingredient[result] = result
            return HttpResponseRedirect('fridgelookup:detail', args=(fridge.id,))
    else:
        form = FridgeForm2()
    return render(request, 'fridgelookup/detail.html', {'fridge_id':fridge_id})"""



    if request.method == "POST":
        form = FridgeForm2(request.POST, instance=fridge)
        print("got to 37")
        if form.is_valid():
            print("got to 39")
            fridge = form.save()
            fridge.ingredients[fridge.staged_ingr] = fridge.staged_amt
            #fridge.staged = ""
            fridge.save()
            return HttpResponseRedirect(reverse('fridgelookup:detail', args=(fridge.id,)))
        #new_ingredient.fridge = Fridge.objects.get(pk=fridge_id)
        #new_ingredient.save()
        #form.save_m2m()
    else:
        form = FridgeForm2(request.POST, instance=fridge)

    return render(request, 'fridgelookup/detail.html', {'form': form, 'fridge': fridge})    
    #return HttpResponse(response % fridge_id)
    #return HttpResponseRedirect(reverse('fridgelookup:detail', args=(fridge.id,)))
    #return render(request, 'fridgelookup/update.html', {'fridge': Fridge.objects.get(pk=fridge_id)})