"""
URL configuration for instagram_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from user.views import RegistrationView, LoginView, MakeLoginView, MakeRegistrationView, HomeView, MyProfilePageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', RegistrationView.as_view(), name='registration-url'),
    path('make-registration/', MakeRegistrationView.as_view(), name='make-registration-url'),
    path('login/', LoginView.as_view(), name='login-url'),
    path('make-login/', MakeLoginView.as_view(), name='make-login-url'),
    path('profile/', MyProfilePageView.as_view(), name='profile-url'),
    path('home/', HomeView.as_view(), name='home-url'),
    path('create-new-post/', CreateNewPostView.as_view(), name='create-new-post-url')

    # path('reels/', ReelsView.as_view(), name='reels-url'),
    # path('create-new-post/', CreateNewPostView.as_view(), name='create-new-post-url')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
