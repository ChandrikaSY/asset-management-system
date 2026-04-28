from django.shortcuts import render, redirect
from .models import Employee, Asset, Assignment

from django.contrib.auth.models import User

# Create admin automatically (runs once)
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@gmail.com", "Admin@123")
    
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        employee = Employee.objects.filter(email=email).first()

        if employee:
            if employee.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('employee_dashboard', employee_id=employee.id)

    return render(request, 'login.html')


def admin_dashboard(request):
    employees = Employee.objects.count()
    assets = Asset.objects.count()
    assigned = Assignment.objects.count()

    return render(request, 'admin_dashboard.html', {
        'employees': employees,
        'assets': assets,
        'assigned': assigned
    })


def employee_dashboard(request, employee_id):
    assignments = Assignment.objects.filter(employee_id=employee_id)

    return render(request, 'employee_dashboard.html', {
        'assignments': assignments
    })