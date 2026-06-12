"""
URL configuration for meditrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/',
        include('patients.urls')
    ),
    path(
        'api/',
        include('doctors.urls')
    ),
     path(
        'api/',
        include('appointments.urls')
    ),
     path(
        'api/',
        include('reports.urls')
    ),
    path(
       'api/hospitals/',
       include('hospitals.urls')
    ),
    path(
       'api/prescriptions/',
       include('prescriptions.urls')
    ),
    path(
       'api/notifications/',
       include('notifications.urls')
    ),
     path(
       'api/emergency/',
       include('emergency.urls')
    ),
    path(
       'api/diets/',
       include('diets.urls')
    ),
     path(
       'api/dashboard/',
       include('dashboard.urls')
    ),
     path('api-auth/', include('rest_framework.urls')),
    # JWT Login
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    # JWT Refresh
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    
]
