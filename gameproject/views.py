from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

class Desarrollador:
    def __init__(self, name: str, surname: str) -> None:
        """Declaro los atributos de clase"""
        self.name = name
        self.surname = surname


def dameFecha(request):
    now = datetime.datetime.now()
    html = "<html><body>Hoy es %s de %s de %s .</body></html>" % now.day, now.month, now.year
    return HttpResponse(html)

def combat(request): 
    # 1º Ejemplo de como cargar templates en las vistas incluyendo como pasar parametros al template.
    #doc_externo = open("C:/Users/Kuach/Desktop/Nuevacarpeta/gameproject/templates/combat.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()
    #ctx = Context({"nombre_desarrollador":desarrollador.name, "apellido_desarrollador":desarrollador.surname, "fecha":now})
    #documento = plt.render(ctx)
    #ctx = Context({"nombre_desarrollador":desarrollador.name, "apellido_desarrollador":desarrollador.surname, "fecha":now})
    #documento = combatTemplate.render(ctx)

    desarrollador = Desarrollador("Jandro", "Ponce")
    now = datetime.datetime.now()

    # 2º Ejemplo de como cargar templates en las vistas, con el metodo get_template que hay en loader (from django.template.loader import get_template)...
    #... y en el fichero settings del proyecto, agregar la ruta de la carpeta donde estén las plantillas (en mi caso "templates")...
    #... en la lista "DIRS" del apartado TEMPLATES.
    combatTemplate = get_template('combat.html')    
    documento = combatTemplate.render({"nombre_desarrollador":desarrollador.name, "apellido_desarrollador":desarrollador.surname, "fecha":now})

    return HttpResponse(documento)