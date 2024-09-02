from django.shortcuts import render


def index(request):
	return render(request, 'pages/index.html')

def bad_request_view(request, exception):
	return render(request, 'pages/404.html', status=404)

def permission_denied_view(request, exception):
	return render(request, 'pages/403.html', status=403)
