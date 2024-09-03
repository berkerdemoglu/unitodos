from django.urls import path

from . import views


urlpatterns = [
    # Log in page
    path('login/', views.LoginView.as_view(), name='login'),
    # Log out page
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # Sign up page
    path('signup/', views.SignupFormView.as_view(), name='signup'),
    # Sign up success page
    path('signup-success/', views.SignupSuccessView.as_view(), name='signup-success')
]
