from django import forms
from .models import Post


class PostCreateForm(form.ModelForm):
    class meta:
        # se especifica el modelo que se quiere manipular para este formulario
        model = Post

        # indico los campos que quiero mostrar
        # son los declarados en 'blog/models.py'
        fields = ('title', 'content')







