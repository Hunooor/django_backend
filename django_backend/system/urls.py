from django.urls import path

from .views import check_server_endpoint

urlpatterns = [
    path('checkserverendpoint', check_server_endpoint)
]
