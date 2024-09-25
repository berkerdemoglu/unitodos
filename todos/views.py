from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from .models import LectureTodo


class TodosView(LoginRequiredMixin, TemplateView):
	template_name = "todos/todos.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['lecture_todos'] = LectureTodo.objects.all()
		return context
