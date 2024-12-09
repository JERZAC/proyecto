from rest_framework.routers import DefaultRouter
from .views import RecetaViewSet, IngredienteViewSet, CategoriaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register('recetas', RecetaViewSet)
router.register('ingredientes', IngredienteViewSet)
router.register('categorias', CategoriaViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = router.urls
