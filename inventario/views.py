from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def lista_productos(request):
    productos = Producto.objects.all()

    return render(
        request,
        'inventario/lista_productos.html',
        {'productos': productos}
    )

@login_required
def crear_producto(request):

    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_productos')

    else:
        form = ProductoForm()

    return render(
        request,
        'inventario/form_producto.html',
        {'form': form}
    )
@login_required
def editar_producto(request, id):

    producto = get_object_or_404(
        Producto,
        id=id
    )

    if request.method == 'POST':

        form = ProductoForm(
            request.POST,
            instance=producto
        )

        if form.is_valid():
            form.save()
            return redirect('lista_productos')

    else:

        form = ProductoForm(
            instance=producto
        )

    return render(
        request,
        'inventario/form_producto.html',
        {'form': form}
    )

def eliminar_producto(request, id):

    if not request.user.is_staff:

        return HttpResponseForbidden(
            "No tiene permisos para eliminar."
        )

    producto = get_object_or_404(
        Producto,
        id=id
    )

    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    return render(
        request,
        'inventario/eliminar_producto.html',
        {'producto': producto}
    )