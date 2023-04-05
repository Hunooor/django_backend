from django.urls import path

from .views import get_user_data, update_user_data

urlpatterns = [
    path('me', get_user_data),
    path('update', update_user_data),
]
