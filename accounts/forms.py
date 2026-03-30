from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'width:100%;padding:0.6rem 0.9rem;background:#1a1a26;border:1px solid #2a2a3a;border-radius:8px;color:#c7c7d4;font-size:0.95rem;outline:none;'
            })