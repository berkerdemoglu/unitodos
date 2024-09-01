from django.contrib import admin

from todos.models import (
	Module, LectureTodo
	)

# Register the models
admin.site.register(Module)
admin.site.register(LectureTodo)
