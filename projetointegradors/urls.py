"""
URL configuration for projetointegrador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin #cria o painel admin com a biblioteca python
from django.urls import path
from . import views

urlpatterns = [ #ROTAS
    path('', views.index, name='index'),# insere index funçao dentro de views
    path('topics', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),#rota para views
    path('home', views.home, name='home'),# insere nome= home  funçao dentro de views
    path('new_topic', views.new_topic, name='new_topic'),# insere NewTopic na views, foi criada para formulario
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'), #depois crie essa função na view
]
