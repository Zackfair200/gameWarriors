from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Desarrollador:
    def __init__(self, name: str, surname: str) -> None:
        """Declaro los atributos de clase"""
        self.name = name
        self.surname = surname

def index(request):
    return render(request, 'index.html')

def combat(request): 
    # 1º Ejemplo de como cargar templates en las vistas incluyendo como pasar parametros al template.
    #doc_externo = open("C:/Users/Kuach/Desktop/Nuevacarpeta/gameproject/templates/combat.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()
    #ctx = Context({"nombre_desarrollador":desarrollador.name, "apellido_desarrollador":desarrollador.surname, "fecha":now})
    #documento = plt.render(ctx)
    #ctx = Context({"nombre_desarrollador":desarrollador.name, "apellido_desarrollador":desarrollador.surname, "fecha":now})
    #documento = combatTemplate.render(ctx)

    # 2º Ejemplo de como cargar templates en las vistas, con el metodo get_template que hay en loader (from django.template.loader import get_template)...
    #... y en el fichero settings del proyecto, agregar la ruta de la carpeta donde estén las plantillas (en mi caso "templates")...
    #... en la lista "DIRS" del apartado TEMPLATES.
    #combatTemplate = get_template('combat.html')    
    #documento = combatTemplate.render({"nombre_desarrollador":desarrollador.name, "apellido_desarrollador":desarrollador.surname, "fecha":now})

    desarrollador = Desarrollador("Jandro", "Ponce")
    now = datetime.datetime.now()

    # 3º Ejemplo para cargar templates (el que vamos a usar en esta view), importando render (from django.shortcuts import render)...
    #... en este ejemplo (como está explicado en el ejemplo 2), ha de estar marcada la ruta donde tenemos los templates en el fichero settings.
    return render(request, 'combat.html', {"nombre_desarrollador":desarrollador.name, "apellido_desarrollador":desarrollador.surname, "fecha":now, })

def contact(request):
    return render(request, 'contact.html')