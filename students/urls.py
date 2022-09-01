from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('add_student', views.add_student, name='add_student'),
    path('login', views.login_request, name='login_request'),
    path("logout", views.logout_request, name= "logout"),
    path('user/dashboard', views.student_login, name='student_login'),

]