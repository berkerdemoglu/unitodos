from django.contrib.auth import views as auth_views
from django.http import HttpResponseNotAllowed


class LoginView(auth_views.LoginView):
	template_name = 'userauth/login.html'
	redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
	template_name = 'userauth/logout.html'

	def get(self, *args, **kwargs):
		"""
		A GET request to logout view should return a HTTP status code of
		405 Method Not Allowed, as we want logout to be only possible
		with a POST request, not GET.
		"""
		return HttpResponseNotAllowed(['POST']) 
