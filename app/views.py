from django.shortcuts import render
from .serializer import PersonaForm

def ingresar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a una página de éxito o mostrar un mensaje de éxito
    else:
        form = PersonaForm()
    return render(request, 'app.html', {'form': form})
