from rest_framework.routers import DefaultRouter

from .views import DietViewSet

router = DefaultRouter()

router.register(
    '',
    DietViewSet
)

urlpatterns = router.urls