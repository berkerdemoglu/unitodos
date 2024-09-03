from django.urls import path

from . import views


urlpatterns = [
    # Login page
    path('login/', views.LoginView.as_view(), name='login'),

    # Logout page
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
