from django.urls import path, include

from LogiSolutions.warehouse.views import CreateWarehouseView, DeleteWarehouseView, EditWarehouseView, \
    DetailsWarehouseView

urlpatterns = (
    path('create/', CreateWarehouseView.as_view(), name='create warehouse'),
    path('<int:pk>/', include([
        path('details/', DetailsWarehouseView, name='details warehouse'),
        path('edit/', EditWarehouseView, name='edit warehouse'),
        path('delete/', DeleteWarehouseView, name='delete warehouse')
    ]))
)
