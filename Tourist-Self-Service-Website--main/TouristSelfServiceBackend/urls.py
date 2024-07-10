"""TouristSelfServiceBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    path('api/', include('Attraction.urls')),
    path('api/', include('Tourist.urls')),
    path('api/', include('Agency.urls')),
    path('api/', include('Route.urls')),
    path('api/', include('Rt_At.urls')),
    path('api/', include('Rt_Rq.urls')),
    path('api/', include('Reservation.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # swagger接口文档
    path('api-doc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # redoc接口文档

]
