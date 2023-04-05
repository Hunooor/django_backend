from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/', include('auth.urls'), name='site authentications'),
    path('system/', include('system.urls'), name='general system endpoints'),
]
