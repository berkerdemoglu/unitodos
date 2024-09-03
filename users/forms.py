from django.contrib.auth.forms import UserCreationForm as DjUserCreationForm
from .models import User, UserProfile


class UserCreationForm(DjUserCreationForm):
    class Meta(DjUserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        # Save user and store it to return later
        new_user = super().save(commit=commit)
        # Create user profile
        UserProfile.objects.create(owner=new_user)
        # Return saved user
        return new_user
