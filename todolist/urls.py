from django.urls import path    
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('completar_tarea/<int:task_id>/', views.complete_task, name='completar_tarea'),
    path('borrar_tarea/<int:task_id>/', views.delete_task, name='borrar_tarea'),

]