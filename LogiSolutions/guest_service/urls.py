from django.urls import path

from LogiSolutions.guest_service.views import AskQuestionView

urlpatterns = (
    path('LogiSolutions/', AskQuestionView.as_view(), name='GuestView'),
)
