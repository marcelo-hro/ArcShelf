from django.db import models
from django.contrib.auth.models import User



class Genero(models.Model):
    name = models.CharField("Nome", max_length=80, unique=True)

    def __str__(self):
        return self.name



class Obra(models.Model):
    FORMAT_CHOICES = [
        ("BOOK", "Livro (Páginas)"),
        ("WEBNOVEL", "Web Novel (Capítulos)"),
    ]
    title = models.CharField("Título", max_length=255, unique=True)
    format_type = models.CharField("Formato", max_length=15, choices=FORMAT_CHOICES, default="BOOK")
    author = models.CharField("Autor", max_length=150)
    total_units = models.PositiveIntegerField("Total de Páginas/Capítulos")
    genres = models.ManyToManyField(Genero, verbose_name="Gêneros")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_format_type_display()})"

# Create your models here.
