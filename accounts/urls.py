from django.urls import path,include

from accounts.views import LoginEmployee,Logout,ClientView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'client',ClientView,basename='client')


urlpatterns = [
    path('login/employee/',LoginEmployee.as_view(),name='login_employee'),
    path('logout/',Logout.as_view(),name='logout'),
    path('',include(router.urls)),
]