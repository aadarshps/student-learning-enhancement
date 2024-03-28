from django.urls import path

from accounts import views


urlpatterns = [
    path('student-signup',views.student_signup,name='student-signup'),
    path('students',views.student_views,name='students'),

]
