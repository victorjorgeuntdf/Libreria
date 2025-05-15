from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

def libro_view(request):
    form = LibroForm()
    libros = Libro.objects.all().order_by('-id')

    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro-view')

    return render(request, 'catalogo/libro_view.html', {'form': form, 'libros': libros})
