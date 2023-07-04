from django.urls import path #importa a função de encaminhar novos caminhos
from . import views  # O . indica da pasta que eu estou importe views

urlpatterns = [
    path('home/', views.home, name="home")
]