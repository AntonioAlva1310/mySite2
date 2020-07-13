from django.urls import path
from school import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('classrooms', views.clasrooms, name='clasrooms'),
    path('classroom_selected/<int:classroom_id>/', views.show_by_class_page, name='classroom_selected')
]