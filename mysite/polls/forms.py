from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateNewUserForm(UserCreationForm):
    username = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    password1 = forms.CharField(required = True)
    password2 = forms.CharField(required = True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def save(self, commit=True):
        user = super(CreateNewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    