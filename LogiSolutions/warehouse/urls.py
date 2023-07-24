from django.urls import path, include

from LogiSolutions.warehouse.views import CreateWarehouseView, DeleteWarehouseView, EditWarehouseView, \
    DetailsWarehouseView

urlpatterns = (
    path('create/', CreateWarehouseView.as_view(), name='create warehouse'),
    path('<int:pk>/', include([
        path('details/', DetailsWarehouseView.as_view(), name='details warehouse'),
        path('edit/', EditWarehouseView.as_view(), name='edit warehouse'),
        path('delete/', DeleteWarehouseView.as_view(), name='delete warehouse')
    ]))
)
