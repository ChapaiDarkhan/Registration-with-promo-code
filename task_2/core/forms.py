from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    promo_code = forms.CharField(help_text='Required if already have 5 users.')

    class Meta:
        model = User
        fields = ('username', 'promo_code', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        if User.objects.all().count() >= 5:
            self.fields['promo_code'].required = True
        else:
            self.fields['promo_code'].required = False
