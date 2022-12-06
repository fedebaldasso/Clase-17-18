import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader


def saludar(request):
    return HttpResponse("Hola mundo!")

def segunda_vista(request):
    return HttpResponse("Ya entendí!! Esto parece ser muy simple! :D")

def dia_de_hoy(request):
    dia=datetime.datetime.today()
    cadena=f"Hoy es {dia}"
    return HttpResponse(cadena)

def saludo_con_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre} como estas?")

def calcula_anio_nacimiento(request, edad):
    anio_actual=datetime.datetime.today().year
    anio_nacimiento=anio_actual-int(edad)
    return HttpResponse(f"<h1>Usted nació en el año {anio_nacimiento}</h1>")

# def probandoHtml(request):

#     diccionario= {"nombre":"Juan", "apellido":"Perez", "edad":"25", "lista_de_notas":[5,2,8,7,1,10,3,9]}
#     archivo=open("C:/Users/Fede/Documents/Cursos Coderhouse/Python/Clase 17/Proyecto_1/Plantillas/template1.html")

#     template=Template(archivo.read())
#     archivo.close()
#     contexto=Context(diccionario)

#     documento=template.render(contexto)#Llena mis espacios en blanco con los datos de mi contexto
#     return HttpResponse(documento)

def probandoHtml(request):

    diccionario= {"nombre":"Juan", "apellido":"Perez", "edad":"25", "lista_de_notas":[5,2,8,7,1,10,3,9]}
    
    template= loader.get_template("template1.html") #Abre, lee y cierra el archivo

    documento=template.render(diccionario)#Llena mis espacios en blanco con los datos de mi contexto
    return HttpResponse(documento)