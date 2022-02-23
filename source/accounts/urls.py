from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

# from accounts.views import login_view, logout_view
from accounts.views import RegisterView, UserProfileView, UpdateUserView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name="registration"),
    path('<int:pk>/', UserProfileView.as_view(), name="user-profile"),
    path('update/', UpdateUserView.as_view(), name="update-user"),
    path('change-password/', UserPasswordChangeView.as_view(), name="change-password")
]
