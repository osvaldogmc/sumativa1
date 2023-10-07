from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    if request.POST:
        Operador1 = int(request.POST['operador1'])
        Operador2 = int(request.POST['operador2'])
        Operacion = request.POST['operacion']
        context = {
            'operador1': Operador1,
            'operador2': Operador2,
            'operacion': Operacion,
            'resultado': 0
        }
        if Operacion == 'suma':
            context['resultado'] = Operador1 + Operador2
        elif Operacion == 'resta':
            context['resultado'] = Operador1 - Operador2
        elif Operacion == 'multi':
            context['resultado'] = Operador1 * Operador2
        elif Operacion == 'divi':
            context['resultado'] = Operador1 / Operador2
    return render(request, 'index.html', context)