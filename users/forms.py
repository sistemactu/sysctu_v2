from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
			'is_staff',
            'password1',
            'password2',
        )