from django.db import models

class Employee(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=100)
    asset_code = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    is_assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset} -> {self.employee}"