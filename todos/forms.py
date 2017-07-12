from django import forms

from todos.models import Todo

from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ['created_at', 'is_achieved', 'user']
        #
        # fields = ['title', 'text']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
