from django.urls import path

from .views import Dashboard
from .routers import router


urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]
