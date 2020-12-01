"""tweeter URL Configuration

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
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views

from apps.core.views import frontpage, signup
from apps.feed.views import TweetCreateView, UserTweetListView

urlpatterns = [
    path('', frontpage, name="frontpage"),

    path('login/', views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', views.LogoutView.as_view(), name="logout"),

    path('feed/', login_required(TweetCreateView.as_view()), name='feed'),

    path('feed/<str:user>/', login_required(UserTweetListView.as_view()), name='feed'),

    # admin
    path('admin/', admin.site.urls),
]
