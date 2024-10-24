"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),  # dj-rest-auth for login, logout, etc.
    path('api/social/', include('allauth.socialaccount.urls')),  # Social Auth
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Provides registration
    path('api/accounts/auth/google/', include('allauth.socialaccount.urls')),  # Google login
    path('api/accounts/auth/facebook/', include('allauth.socialaccount.urls')),  # facebook login

]

