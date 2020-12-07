from django.urls import path
from tags.views import Tags
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tags',Tags)
urlpatterns = router.urls