from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    listo = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list':listo})

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
    return redirect('/lists/%d/' % (listo.id,))

def add_item(request,list_id):
    listo = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=listo)
    return redirect('/lists/%d/' % (listo.id,))