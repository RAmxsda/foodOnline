from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register, name='registerUser'),
    path('registerVendor/',views.registerVendor, name='registerVendor'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/',views.myAccount, name='myAccount'),
    path('cust-dashboard/', views.custDashboard, name='custDashboard'),
    path('vendor-dashboard/', views.vendorDashboard, name='vendorDashboard'),

]