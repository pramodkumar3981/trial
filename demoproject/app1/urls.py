from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ="home"),
    path('home2',views.home2,name='home2'),
    path('signup/',views.signup,name = 'signup'),
    path('contact/',views.contact, name = 'contact'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('newsletter/',views.newsletter, name='newsletter'),
    path('updateprofileuser/',views.updateuser,name='updateuser'),
    path('search/',views.search, name='search'),
    path('myaccount/',views.myaccount, name = 'myaccount'),

]
