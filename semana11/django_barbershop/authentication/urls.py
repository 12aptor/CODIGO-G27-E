from django.urls import path
from .views import *

urlpatterns = [
    path('roles/', RoleView.as_view()),
    path('roles/<int:pk>/', ManageRoleView.as_view()),
    path('auth/register/', RegisterView.as_view()),
    # path('auth/login/', LoginView.as_view()),
]