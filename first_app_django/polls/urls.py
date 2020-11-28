from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #url base: http://localhost:8000/polls
    
    #ex: /
    path('', views.IndexView.as_view(), name='index'),  # esto es una vista generica
    #ex: /5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), #question_id es enviado como parametro a views.detail, esto es una vista generica
    # ex: /5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), #question_id es enviado como parametro a views.results, esto es una vista generica
    # ex: /5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'), #question_id es enviado como parametro a views.vote
    ]


'''
Cuando alguien solicita una página desde su sitio web - digamos, «/polls/34/», Django cargará el módulo Python mysite.urls porque está señalado 
por la configuración ROOT_URLCONF. Él encuentra la variable llamada urlpatterns y recorre las expresiones regulares en orden. Cuando encuentra la 
coincidencia 'polls/' retira el texto que coincide ("polls/") y envía el texto restante - "34/" - a la URLconf “polls.urls” para seguir siendo procesado. 
Allí la coincidencia '<int:question_id>/' resulta en una llamada a la vista detail() de la siguiente forma:

detail(request=<HttpRequest object>, question_id=34)

El proyecto tutorial solo tiene una aplicación; polls. En proyectos reales de Django, puede haber cinco, diez, veinte o más aplicaciones. ¿Cómo diferencia 
Django los nombres de las URLs entre ellos? Por ejemplo, la aplicación polls tiene una vista detail, como la podría tener también una aplicación en el mismo 
proyecto que es para un blog. ¿Cómo hacer para que Django sepa cual vista de aplicaciones crear para una URL cuando se utiliza la etiqueta de plantilla`` {% url%}``?

La solución es añadir espacios de nombres a su URLconf. En el archivo polls/urls.py, añada un app_name para configurar el espacio de nombres de la aplicación: app_name = 'polls'
'''