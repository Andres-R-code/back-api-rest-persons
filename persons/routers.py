from rest_framework.routers import DefaultRouter

from persons.views import PersonsViewSet

router = DefaultRouter()

router.register(r'persons',PersonsViewSet,basename = 'persons')


urlpatterns = router.urls