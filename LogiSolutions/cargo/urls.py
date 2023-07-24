from django.urls import path, include

from LogiSolutions.cargo.views import CreateCargoView, DetailsCargoView, EditCargoView, DeleteCargoView

urlpatterns = (
    path('create/', CreateCargoView.as_view(), name='create cargo'),
    path('<int:pk>/', include([
        path('details/', DetailsCargoView.as_view(), name='details cargo'),
        path('edit/', EditCargoView.as_view(), name='edit cargo'),
        path('delete/', DeleteCargoView.as_view(), name='delete cargo')
    ]))
)
