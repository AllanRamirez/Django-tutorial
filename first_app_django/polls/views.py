#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question

# Create your views here.

#cada funcion creada aqui es denominada como una vista 
def index(request):
    #esta es la practica mas comun para hacer esto (objeto render). Usando esto, no es necesario cargar HttpResponse ni loader.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    #La función render() toma el objeto solicitado como su primer argumento, un nombre de plantilla como su segundo argumento 
    # y un diccionario como su tercer argumento opcional. La función retorna un objeto HttpResponse de la plantilla determinada creada con el contexto dado.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #utilizando render() y validando error 404 con la practica mas utilizada (nos da bajo acomplamiento) cpm el try catch se genera un acoplamiento entre la capa de vistas y modelos
    #También hay una función get_list_or_404() , que funciona igual que get_object_or_404() - excepto usando filter() en lugar de get(). La misma levanta la excepción Http404 si la lista está vacía.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


'''
Su vista puede leer registros de una base de datos o no, puede usar un sistema de plantillas como el de Django o un sistema de plantillas Python de terceros o no. 
Puede generar un archivo PDF, salida XML, crear un archivo ZIP en la marcha, todo lo que quiera, utilizando cualquier librería de Python que desee.

Todo lo que Django quiere es, ese objeto HttpResponse o una excepción.
'''

