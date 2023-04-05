from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth.urls'), name='site authentications'),
    path('system/', include('system.urls'), name='general system endpoints'),
    path('user/', include('users.urls'), name='user model endpoints'),
]
