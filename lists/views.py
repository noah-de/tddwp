from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from lists.forms import ExistingListItemForm, ItemForm
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    listo = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=listo)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=listo, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(listo)
    return render(request, 'list.html', {'list': listo, "form": form})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        listo = List.objects.create()
        form.save(for_list=listo)
        return redirect(listo)
    else:
        return render(request, 'home.html', {"form": form})

