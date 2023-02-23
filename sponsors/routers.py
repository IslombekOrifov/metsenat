from rest_framework import routers

from .views import SponsorModelViewSet

router = routers.DefaultRouter()

router.register('', SponsorModelViewSet)