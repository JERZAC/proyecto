from rest_framework.viewsets import ModelViewSet
from .models import Receta, Ingrediente, Categoria, Usuario
from .serializers import RecetaSerializer, IngredienteSerializer, CategoriaSerializer, UsuarioSerializer

class RecetaViewSet(ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class IngredienteViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
