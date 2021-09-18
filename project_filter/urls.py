"""project_filter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Import admin module
from django.contrib import admin
# Import path and include module
from django.urls import path, include
# Import SearchEmployee module
from filterapp.views import SearchEmployee

urlpatterns = [
    # Define the path for admin
    path('admin/', admin.site.urls),
    # Define the path for search
    path('searchEmp/', SearchEmployee.as_view()),
]
