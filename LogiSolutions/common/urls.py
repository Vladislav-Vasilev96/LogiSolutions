from django.urls import path, include

from LogiSolutions.common.views import IndexView, CargoCatalog, VehicleCatalog, WarehouseCatalog

urlpatterns = (
    path('', IndexView.as_view(), name='IndexView'),
    path('catalog/', include([
        path('cargo/', CargoCatalog.as_view(), name='CargoCatalogView'),
        path('vehicle/', VehicleCatalog.as_view(), name='VehicleCatalogView'),
        path('warehouse/', WarehouseCatalog.as_view(), name='WarehouseCatalogView'),
    ]))
)
