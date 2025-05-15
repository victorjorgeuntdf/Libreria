from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.libro_view, name='libro-view'),
]
