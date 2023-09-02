from django import forms
from .models import Post
from django.utils import timezone

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','etiqueta_tarea','author', 'content',  'tzone', 'observations', 'fecha_limite']
        widgets = {
            'fecha_limite': forms.DateInput( attrs={'type': 'date' , 'value': f'{timezone.now().date()}'}),
        }



