from django.urls import path, include

from LogiSolutions.vehicle.views import CreateVehicleView, DetailsVehicleView, DeleteVehicleView, EditVehicleView

urlpatterns = (
    path('create/', CreateVehicleView.as_view(), name='create vehicle'),
    path('<int:pk>/', include([
        path('details/', DetailsVehicleView.as_view(), name='details vehicle'),
        path('edit/', EditVehicleView.as_view(), name='edit vehicle'),
        path('delete/', DeleteVehicleView.as_view(), name='delete vehicle')
    ]))
)
