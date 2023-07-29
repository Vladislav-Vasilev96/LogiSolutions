from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserCreationForm

from LogiSolutions.accounts.models import Profile, CustomUser

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': 'Password'
            }
        ),
        label='Password:')
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password2'
            }
        ),
        label='Repeat password:')

    class Meta:
        model = CustomUser
        fields = ['email', ]
        widgets ={
            'email':forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
        }


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile.objects.create(user=user, email=user.email)
            profile.save()
        return user


class ChangePasswordForm(auth_forms.PasswordChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
