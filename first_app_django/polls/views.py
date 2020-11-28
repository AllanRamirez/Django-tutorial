#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.views import generic

from .models import Question, Choice

# Create your views here.

#cada funcion o clase(vistas genericas) creada aqui es denominada como una vista 
class IndexView(generic.ListView): # generic.ListView: mostrar una lista de objetos
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView): # generic.DetailView: mostrar una página de detalles para un tipo específico de objeto
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    '''
    Esta es la practica mas comun para hacer esto (objeto render()). Usando esto, no es necesario cargar HttpResponse ni loader.
    La función render() toma el objeto solicitado como su primer argumento, un nombre de plantilla como su segundo argumento 
    y un diccionario como su tercer argumento opcional. La función retorna un objeto HttpResponse de la plantilla determinada creada con el contexto dado.
    
    utilizando render() y validando error 404 con la practica mas utilizada (nos da bajo acomplamiento) cpm el try catch se genera un acoplamiento entre la capa de vistas y modelos
    También hay una función get_list_or_404() , que funciona igual que get_object_or_404() - excepto usando filter() en lugar de get(). La misma levanta la excepción Http404 si la lista está vacía.
    '''
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # request.POST['choice'] retorna la ID de la opción seleccionada como una cadena
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1 #avoiding-race-conditions-using-f
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) # -> /polls/3/results/


'''
Su vista puede leer registros de una base de datos o no, puede usar un sistema de plantillas como el de Django o un sistema de plantillas Python de terceros o no. 
Puede generar un archivo PDF, salida XML, crear un archivo ZIP en la marcha, todo lo que quiera, utilizando cualquier librería de Python que desee.

Todo lo que Django quiere es, ese objeto HttpResponse o una excepción.
'''

