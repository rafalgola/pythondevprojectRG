"""
URL configuration for projektzaliczeniowy project.

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
from django.urls import path
from walidator import views as apiview


urlpatterns = [
    path('', apiview.display_message, name='display_message'),
    path('Pesel', apiview.validate_pesel, name='validate_pesel'),
    path('Assertions', apiview.list_asserted_pesels, name='list_asserted_pesels'),
    path('admin/', admin.site.urls),
]
