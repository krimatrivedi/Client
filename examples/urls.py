from django.urls import path
from .views import  register,dashboard,client,Projects,Dashboard1

from . import views
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

urlpatterns = [
  
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('Dashboard1/', Dashboard1, name='Dashboard1'),
    path('client/', client, name='client'),
    path('Projects/', Projects, name='Projects'),
    path('_books_table/', views.Client.as_view(), name='_books_table'),
    path('Projecttable/', views.ProjectDetails.as_view(), name='Projecttable'),
    path('client_details/', views.ClientDetails.as_view(), name='client_details'),
    path('create_book/', views.BookCreateView.as_view(), name='create_book'),
    path('create_project/', views.ProjectCreateView.as_view(), name='create_project'),
    path('books/', views.books, name='books'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]
