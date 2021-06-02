"""intern_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
import accounts.views as a_views
import task_app.views as ta_views
import task_2.views as t2_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', a_views.index, name='index'),
    path('home/', a_views.home, name="home"),
    path('upload_task/', ta_views.upload, name="upload"),
    path('display_task/', ta_views.display, name="display"),
    path('logout/', a_views.logout_user, name='logout'),
    path('signUp/', a_views.register, name='register'),
    path('signIn/', a_views.login_user, name='login'),
    path('hierarchy/', t2_views.hierarchy, name='hierarchy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

