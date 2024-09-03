from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import UserCreationForm


class LoginView(auth_views.LoginView):
	template_name = 'userauth/login.html'
	redirect_authenticated_user = True

	def dispatch(self, request, *args, **kwargs):
		"""Don't let the user log in if already authenticated"""
		if request.user.is_authenticated:
			return redirect('pages:index')
		return super().dispatch(request, *args, **kwargs)


# TODO: Add 'successfully logged out view'
class LogoutView(auth_views.LogoutView):
	template_name = 'userauth/logout.html'

	def get(self, *args, **kwargs):
		"""
		A GET request to logout view should return a HTTP status code of
		405 Method Not Allowed, as we want logout to be only possible
		with a POST request, not GET.
		"""
		return HttpResponseNotAllowed(['POST'])


class SignupFormView(FormView):
	template_name = 'userauth/signup.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('users:signup-success')

	def form_valid(self, form):
		"""
		Received a valid user creation form, authenticate and save the user, 
		log them in, keep track of their signup status through session info 
		and redirect them to the success page.
		"""
		# Save the user
		form.save()
		# Authenticate user
		username = self.request.POST['username']
		password = self.request.POST['password1']
		user = authenticate(username=username, password=password)
		# Log them in
		login(self.request, user)
		# Set signup tracking flag
		self.request.session['signup_complete'] = True
		return super().form_valid(form)

	def dispatch(self, request, *args, **kwargs):
		"""Don't let the user sign up if they are already logged in"""
		if request.user.is_authenticated:
			return redirect('pages:index')
		return super().dispatch(request, *args, **kwargs)


class SignupSuccessView(TemplateView):
	template_name = 'userauth/signup_success.html'

	def dispatch(self, request, *args, **kwargs):
		"""Check if the user came here after signing up"""
		if request.session.pop('signup_complete', False):  # signed up
			return super().dispatch(request, *args, **kwargs)
		return redirect('users:signup')
