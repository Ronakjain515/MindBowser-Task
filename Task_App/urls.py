from django.urls import path
from .views import ManagerLogin, ManagerRegister, Dashboard, CreateEmployee, Logout, EditEmployee


urlpatterns = [
    path('Manager-Login', ManagerLogin.as_view(), name="ManagerLogin"),
    path('Manager-Register', ManagerRegister.as_view(), name="ManagerRegister"),
    path('Logout', Logout.as_view(), name="Logout"),
    path('Dashboard/<int:index>', Dashboard.as_view(), name="Dashboard"),
    path('Create-Employee', CreateEmployee.as_view(), name="CreateEmployee"),
    path('Edit-Employee/<int:empId>', EditEmployee.as_view(), name="EditEmployee"),
]