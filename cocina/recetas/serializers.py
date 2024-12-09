from rest_framework import serializers
from .models import Receta, Ingrediente, Categoria, Usuario

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class RecetaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)

    class Meta:
        model = Receta
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
