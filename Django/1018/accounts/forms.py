from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:

        model=get_user_model()
        fields=('username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):

        model=get_user_model()
        fields=('first_name','last_name','email',)
