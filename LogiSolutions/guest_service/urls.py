from django.urls import path

from LogiSolutions.guest_service.views import GuestUserView

urlpatterns = (
    path('LogiSolutions/', GuestUserView.as_view(), name='GuestView'),
)
