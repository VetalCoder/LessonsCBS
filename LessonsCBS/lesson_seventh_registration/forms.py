from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


# additional form for registration
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('biography', 'birth_date')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }