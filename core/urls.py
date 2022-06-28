from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()

router.register('projeto', viewsets.ProjetoViewSet)

urlpatterns = router.urls
