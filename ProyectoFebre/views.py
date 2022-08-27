from django.http import HttpResponse
from django.template import Context, Template

def familia(request):
    return HttpResponse ('esta es mi familia')

def template_familia(request):
    mihtml = open("C:/Users/HP/Coder - Python/MVTFebre/Plantillas/Template.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)