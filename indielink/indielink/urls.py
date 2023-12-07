"""indielink URL Configuration

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
# main/urls.py
from django.contrib import admin
from django.urls import path, include
from landing import views as landing_views
from login import views as login_views
from game import views as game_views
from game import urls as game_urls
from profiles import views as profile_views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_views.landingpage),
    path('favorites/', landing_views.favorites),
    path('signup/', login_views.signup),
    path('login/', login_views.user_login),
    path('logout/', login_views.user_logout),
    path('create_game/', game_views.create_game),
    path('edit_game/<int:game_id>/', game_views.edit_game),
    path('game_list/', game_views.game_list),
    path('', include(game_urls)),
    path('search/', game_views.genre_search),
    path('add_fav/<int:game_id>/', game_views.add_fav),
    path('remove_fav/<int:game_id>/', game_views.remove_fav),
    path('profile/',profile_views.profile),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
