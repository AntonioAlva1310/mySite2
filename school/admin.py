from django.contrib import admin

# Register your models here.
from school.models import Clasroom, Student


admin.site.register(Clasroom)
admin.site.register(Student)