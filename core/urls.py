from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employee/<int:employee_id>/', views.employee_dashboard, name='employee_dashboard'),
]