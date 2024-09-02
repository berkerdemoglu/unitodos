"""
URL configuration for unitodos project.

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
from django.urls import path, include

from pages.views import (
    bad_request_view, permission_denied_view
    )


urlpatterns = [
    path('admin/', admin.site.urls),

    # pages app
    path('', include(('pages.urls', 'pages'), namespace='pages')),

    # todos app
    path('todos', include(('todos.urls', 'todos'), namespace='todos')),
]

# Error views
handler404 = bad_request_view
handler403 = permission_denied_view
