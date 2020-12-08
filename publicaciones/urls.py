from django.urls import path
from publicaciones.views import Publicacion
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'',Publicacion)
urlpatterns = router.urls