#formulario
from django import forms
from .models import Topic, Entry
#Aqui vc cria as classes do formulario
class TopicForm(forms.ModelForm): #cria classe TopicForm, herda de classe model
    class Meta: #cria classe meta
        model = Topic 
        fields = ['text']
        labels = {'text': ''}#campo vazio para prenchimento do formulario
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}