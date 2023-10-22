from django.urls import path
from .views import HometaskView

urlpatterns = [
    path('home_tasks/', HometaskView.as_view(), name='home_tasks'),
]