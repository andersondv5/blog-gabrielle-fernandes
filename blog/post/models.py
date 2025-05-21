from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Tag(models.Model):
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=20, default="bg-purple-600")

    def __str__(self):
        return self.nome

class Post(models.Model):  # Não herda mais de Page
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    descricao = models.TextField()
    conteudo = models.TextField()  # Usaremos o TinyMCE via Django Admin
    data = models.DateField("Data de publicação")
    data = models.DateTimeField("Data de publicação", default=timezone.now)
    tags = models.ManyToManyField(Tag, blank=True)
    
    class Meta:
        ordering = ['-data']

    def save(self, *args, **kwargs):
        # Geração automática de slug
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo










