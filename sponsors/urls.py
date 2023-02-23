from django.urls import path

from .views import SponsorAddDonateListApiView
from .routers import router

urlpatterns = [
    path('donate/add/', SponsorAddDonateListApiView.as_view()),
]

urlpatterns += router.urls
