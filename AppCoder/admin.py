from django.contrib import admin

from  .models import * #importamos el archivo models


#registramos los modelos

admin.site.register(Curso)

admin.site.register(Estudiante)

admin.site.register(Profesor)

admin.site.register(Entregable)

admin.site.register(Avatar)

