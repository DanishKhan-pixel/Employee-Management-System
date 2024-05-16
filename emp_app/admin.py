from django.contrib import admin
from .models import Employee, role, Dep

# Register your models here.
admin.site.register(Employee)
admin.site.register(Dep)
admin.site.register(role)