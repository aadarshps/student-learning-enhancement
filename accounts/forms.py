from django import forms

from accounts.models import *


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password','email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already in use')
        return username
    
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','mobile_number','date_of_birth','learning_style']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }