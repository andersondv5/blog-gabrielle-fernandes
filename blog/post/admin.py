from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Tag

class PostAdminForm(forms.ModelForm):
    conteudo = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('titulo', 'data', 'slug')
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)


