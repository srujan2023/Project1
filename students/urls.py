
from django.urls import path
from .views import index,register,view_students,update_student,delete_student

urlpatterns = [
   
    path('',index,name='index'),
    path('Register.html/',register,name='register'),
    path('view_students/',view_students,name='view_students'),
    path('update/<int:id>/',update_student,name='update_student'),
    path('delete/<int:id>/',delete_student,name='delete_student')
    
    
    
    
]