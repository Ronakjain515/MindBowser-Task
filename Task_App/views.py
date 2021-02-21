from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import ManagerLoginForm, ManagerRegisterForm, EmployeeForm
from .models import Manager, Employee
from .decorators import Login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator


# Create your views here.

class ManagerLogin(View):

    def get(self, request, *args, **kwargs):
        return render(request, "Login.html")
    
    def post(self, request, *args, **kwargs):

        message = ""    # message for printing errors
        try:
            form = ManagerLoginForm(request.POST)
            if form.is_valid():
                try:
                    manager = Manager.objects.get(email=form.cleaned_data["email"], password=form.cleaned_data["password"])
                    request.session["managerId"] = manager.id
                    return redirect("Dashboard/1")
                except Manager.DoesNotExist:
                    message = "Wrong Credentials.."
            else:
                message = form.errors
        except Exception as e:
            message = e

        return render(request, "Login.html", context={"message": message})


class ManagerRegister(View):

    def get(self, request, *args, **kwargs):
        return render(request, "Register.html")
        
    def post(self, request, *args, **kwargs):

        message = ""    # message for printing errors
        form = ManagerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ManagerLogin")
        else:
            message = form.errors
        return render(request, "Register.html", context={"message": message})


class Logout(View):
    @method_decorator(Login_required)
    def get(self, request, *args, **kwargs):
        del(request.session["managerId"])
        return redirect("ManagerLogin")

class Dashboard(View):

    @method_decorator(Login_required)
    def get(self, request, index, *args, **kwargs):

        employee = Employee.objects.all()
        empPaginator = Paginator(employee, 5)
        empPage = empPaginator.page(index)
        return render(request, "Dashboard.html", context={"employees": empPage})
        
    @method_decorator(Login_required)
    def post(self, request, *args, **kwargs):
        try:
            message = ""
            employee = Employee.objects.all()
            empPaginator = Paginator(employee, 5)
            empPage = empPaginator.page(request.POST["index"])
        
            empId = request.POST["empId"]
            Employee.objects.filter(id=empId).delete()
            return render(request, "Dashboard.html", context={"employees": empPage})
        except Exception as e:
            message = e
        
        return render(request, "Dashboard.html", context={"employees": empPage, "message": message})


class CreateEmployee(View):
    
    @method_decorator(Login_required)
    def get(self, request, *args, **kwargs):
        return render(request, "CreateEmployee.html")
    
    @method_decorator(Login_required)
    def post(self, request, *args, **kwargs):

        message = ""
        try:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "CreateEmployee.html")
            else:
                message = form.errors
        except Exception as e:
            message = e
        return render(request, "CreateEmployee.html", {"message": message})


class EditEmployee(View):

    @method_decorator(Login_required)
    def get(self, request, empId, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=empId)
        except:
            return redirect("/Dashboard/1")
        return render(request, "EditEmployee.html", context={"emp": emp})    

    @method_decorator(Login_required)
    def post(self, request, *args, **kwargs):

        message = ""
        try:
            if request.POST.get("id", None):
                id = request.POST.get("id", None)
                instance = get_object_or_404(Employee, id=id)
                form = EmployeeForm(request.POST or None, instance=instance)
                if form.is_valid():
                    form.save()
                else:
                    message = form.errors
            else:
                message = "incorrect Employee Id"
        except Exception as e:
            message = e
        return render(request, "EditEmployee.html", context={"emp": instance, "message": message})