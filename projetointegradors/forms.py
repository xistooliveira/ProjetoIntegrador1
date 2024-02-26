#formulario
from django import forms
from .models import Topic

class TopicForm(forms.ModelForm): #cria classe TopicForm, herda de classe model
    class Meta: #cria classe meta
        model = Topic 
        fields = ['text']
        labels = {'text': ''}#campo vazio para prenchimento do formulario