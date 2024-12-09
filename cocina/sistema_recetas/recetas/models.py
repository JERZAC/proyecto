from django.db import models

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[
        ('vegetal', 'Vegetal'),
        ('proteina', 'Proteína'),
        ('especia', 'Especia'),
        ('otro', 'Otro'),
    ])
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tiempo_preparacion = models.PositiveIntegerField(help_text="Tiempo en minutos")
    porciones = models.PositiveIntegerField()
    ingredientes = models.ManyToManyField(Ingrediente, related_name="recetas")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="recetas")
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        # Validación personalizada: Tiempo de preparación debe ser mayor a 0
        if self.tiempo_preparacion <= 0:
            raise ValidationError({'tiempo_preparacion': 'El tiempo de preparación debe ser mayor a 0 minutos.'})


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    recetas_creadas = models.ManyToManyField(Receta, blank=True, related_name="creadores")

    def __str__(self):
        return self.nombre
