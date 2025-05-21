from django import forms
from .models import Post
from django.utils.safestring import mark_safe

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descricao', 'conteudo', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full border px-3 py-2 rounded'})


