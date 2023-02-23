from rest_framework import routers

from .views import StudentModelViewSet, AddSponsorModelViewSet

router = routers.DefaultRouter()

router.register('students/', StudentModelViewSet)
router.register('devided/funts/', StudentModelViewSet)