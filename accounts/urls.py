from django.urls import path,include

from accounts.views import LoginEmployee,Logout

urlpatterns = [
    path('login/employee/',LoginEmployee.as_view(),name='login_employee'),
    path('logout/',Logout.as_view(),name='logout'),
]