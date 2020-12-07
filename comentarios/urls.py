from django.urls import path
from comentarios.views import Comentario
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'comentarios',Comentario)
urlpatterns = router.urls