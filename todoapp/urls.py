from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('delete/<int:task>', views.delete, name='delete'),
    path('update/<int:task>', views.update, name='update'),
    path('notes/<int:id>', views.notes, name='notes')



]