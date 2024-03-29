"""
URL configuration for film_project project.

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
from films.views import HomePageView, FilmCreateView, DirectorCreateView, ReviewCreateView, FilmDeleteView, FavoriteFilmView, FilmDetailView
from accounts.views import login_view, logout_view, profile_view, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='homepage'),
    path('homepage', HomePageView.as_view(), name='homepage'),
    path('addFilm/', FilmCreateView.as_view(), name='addFilm'),
    path('addDirector/', DirectorCreateView.as_view(), name='addDirector'),
    path('addReview/<int:pk>/', ReviewCreateView.as_view(), name='addReview'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('delete_film/<int:pk>/', FilmDeleteView.as_view(), name='deleteFilm'),
    path('favoriteFilm/<int:film_id>/',
         FavoriteFilmView.as_view(), name='favoriteFilm'),
    path('film/<int:pk>/', FilmDetailView.as_view(), name='filmDetail'),
    # path('favoriteFilm/<int:pk>/', favorite_film, name='favoriteFilm'),
]
