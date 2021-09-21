from django.urls import path
from .views import home,add_student,delete_student,Editstudent
urlpatterns = [
    path('',home.as_view(),name='home'),
    path('add-student/',add_student.as_view(), name='add-student'),
    path('delete-student/',delete_student.as_view(), name='delete-student'),
    path('edit-student/<int:id>/',Editstudent.as_view(), name='edit-student')

]
