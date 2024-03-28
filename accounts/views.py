import logging
from django.shortcuts import redirect, render

from accounts.forms import *

# Create your views here.
logger = logging.getLogger(__name__)

def admin_dashboard(request):
    return render(request,'admintemp/index.html')

def student_signup(request):
    try:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            u_form = StudentForm(request.POST)
            if form.is_valid() and u_form.is_valid():
                user = form.save(commit=False)
                user.role = 3
                user.is_active = True
                user.save()
                std = u_form.save(commit=False)
                std.user = user
                std.save()
                return redirect('students') 
        else:
            form = UserRegisterForm()
            u_form = StudentForm()
    except Exception as e:
        logger.error(f"An error occurred during signup: {e}")
    return render(request,'admintemp/student_register.html',{'form':form,'u_form':u_form})

def student_views(request):
    try:
        std = User.objects.filter(role=3)
        data = UserProfile.objects.filter(user__in=std)
    except Exception as e:
        logger.error(f"An error occurred during signup: {e}")    
    return render(request,'admintemp/student_view.html',{'data':data})

