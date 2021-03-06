"""
mynotes_settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from notes import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='url_home'),
    path('topics/', views.home, name='url_topics'),
    path('topics/new', views.topic_new, name='url_topic_new'),
# accounts:====================================================
    path('signup/',accounts_views.signup,name='url_signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('topics/<int:topic_id>/edit/', views.topic_edit, name = 'url_topic_edit'),
]
