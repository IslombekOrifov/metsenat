from rest_framework import routers

from .views import HeiModelViewSet


router = routers.SimpleRouter()

router.register('university/', HeiModelViewSet)

