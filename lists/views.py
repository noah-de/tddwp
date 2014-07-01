from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    listo = List.objects.get(id=list_id)
    error = None
    
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'],list=listo)
            item.full_clean()
            item.save()
            return redirect(listo)
        except ValidationError:
            error = "You can't have an empty list item"
    return render(request, 'list.html', {'list':listo, 'error':error})

def new_list(request):
    listo = List.objects.create()
    item = Item(text=request.POST['item_text'],list=listo)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        listo.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(listo)

def add_item(request,list_id):
    listo = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=listo)
    return redirect('/lists/%d/' % (listo.id,))