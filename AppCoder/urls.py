
from django.urls import path
from AppCoder import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('', views.inicio,name="Inicio"),
    path('cursos', views.cursos,name="Cursos"),
    path('profesores', views.profesores,name="Profesores"),
    path('estudiantes', views.estudiantes,name="Estudiantes"),
    path('entregables', views.entregables,name="Entregables"),
    path('busquedaCamada',views.busquedaCamada,name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('leerCursos', views.leerCursos,name="LeerCursos"),
    path('eliminarCursos/<curso_nombre>/', views.eliminarCursos,name="EliminarCurso"),
    path('editarCurso/<curso_nombre>/', views.editarCurso,name="EditarCurso"),
    path('profesor/list',views.ProfesorList.as_view(),name='List'),
    path(r'(?P<pk>\d+)$',views.ProfesorDetalle.as_view(),name='Detail'),
    path(r'^nuevo$',views.ProfesorCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.ProfesorUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.ProfesorDelete.as_view(),name='Delete'),
    path('login',views.login_request,name='Login'),
    path('register',views.register,name='Register'),
    path('logout',LogoutView.as_view(template_name='AppCoder/logout.html'),name='Logout'),
]