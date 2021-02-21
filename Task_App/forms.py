from django import forms
from .models import Manager, Employee

class ManagerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)


class ManagerRegisterForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'