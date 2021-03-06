"""worldcup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from landing import views as lndviews
from usrauth import views as authviews
from dashboard import views as dashviews
from predictions import views as predictviews

urlpatterns = [
    path('admin/', admin.site.urls),

    # Landing and home page
    path('', lndviews.landing),
    path('home/', lndviews.landing),
    path('landing/', lndviews.landing, name='landing'),

    # User creation and authentication        
    path('signup/', authviews.user_signup, name='user_signup'),
    path('login/', authviews.user_login, name='user_login'),
    path('logout/', authviews.user_logout, name='user_logout'),

    # User Dashboard
    path('dashboard/', dashviews.dashmain, name='dashmain'),
    
    path('user_predictions/', predictviews.user_predictions, name='user_predictions'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
