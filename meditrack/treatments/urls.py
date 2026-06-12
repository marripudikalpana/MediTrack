from rest_framework.routers import DefaultRouter

from .views import TreatmentViewSet

router = DefaultRouter()

router.register(
    '',
    TreatmentViewSet
)

urlpatterns = router.urls