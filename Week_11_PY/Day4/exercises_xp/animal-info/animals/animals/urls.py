"""
URL configuration for animals project.

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
from info import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', views.display_all_animals, name='display_all_animals'),
    path('families/', views.display_all_families, name='display_all_families'),
    path('animal/<int:animal_id>/',
         views.display_one_animal, name='display_one_animal'),
    path('animal_in_family/<int:family_id>/',
         views.display_animal_per_family, name='display_animal_per_family'),
]
