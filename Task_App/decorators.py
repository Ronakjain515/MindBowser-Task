from functools import wraps
from django.shortcuts import redirect

def Login_required(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        print()
        if request.session.get('managerId', None):
             return function(request, *args, **kwargs)
        else:
            return redirect('ManagerLogin')

  return wrap