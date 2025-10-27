from django.urls import path
from .views import activities_root

urlpatterns = [
    path('', activities_root)
]
