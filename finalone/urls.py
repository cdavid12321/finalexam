"""finalone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from final.views import hello_view
from final.views import option_1
from final import views as finalviews, search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('hello/low?sex=2&age=1&job=1&earn=1&hobbit=1', option_1),
    path('search-form$', search.search_form),
    path('search', search.search),


]
