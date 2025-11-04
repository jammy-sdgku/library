from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm

# Create your views here.
def inventory_page(request):
    book_list = Book.objects.all()
    return render(request, 'inventory/inventory.html', {'book_list': book_list})

def inventory_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = BookForm()
    return render(request, 'inventory/add.html', {'form': form})

def inventory_edit(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = BookForm(instance=book)
    return render(request, 'inventory/edit.html', {'form': form, 'book': book})

def inventory_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('inventory')
    return render(request, 'inventory/delete.html', {'book': book})