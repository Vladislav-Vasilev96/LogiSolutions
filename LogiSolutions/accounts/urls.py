from django.urls import path

from LogiSolutions.accounts.views import RegisterUserView, LoginUserView, LogoutUserView, DetailUserView, EditUserView, \
    DeleteUserView, ChangePasswordView, LogoutConfirmationView

urlpatterns = (

    path('register/', RegisterUserView.as_view(), name='RegisterView'),
    path('login/', LoginUserView.as_view(), name='LoginView'),
    path('logout/confirm/', LogoutConfirmationView.as_view(), name='LogoutConfirmationView'),
    path('logout/', LogoutUserView.as_view(), name='LogoutView'),
    path('details/<int:pk>', DetailUserView.as_view(), name='DetailsProfileView'),
    path('edit/<int:pk>', EditUserView.as_view(), name='EditProfileView'),
    path('delete/<int:pk>', DeleteUserView.as_view(), name='DeleteProfileVIew'),
    path('change-password/<int:pk>', ChangePasswordView.as_view(), name='ChangePasswordView'),
)
