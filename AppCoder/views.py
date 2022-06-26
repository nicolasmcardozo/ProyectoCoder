from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Djangooo - Coder")

def saludar_a(request,nombre):   #Nuestra primera vista :) 
	return HttpResponse(f"Hola como estas {nombre.capitalize()}")

def mostrar_mi_template(request):
	return render(request, "AppCoder/index.html")

def curso(self):
	curso = Curso(nombre="SQL",camada=20000)
	curso.save()
	documentoDeTexto=f"--->Curso: {curso.nombre}, Camada: {curso.camada}"

	return HttpResponse(documentoDeTexto)
	
