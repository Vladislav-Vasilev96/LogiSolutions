from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('LogiSolutions.common.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('LogiSolutions.accounts.urls')),
    path('photos/', include('LogiSolutions.photos.urls')),
    path('common/', include('LogiSolutions.common.urls')),
    path('vehicle/', include('LogiSolutions.vehicle.urls')),
    path('cargo/', include('LogiSolutions.cargo.urls')),
    path('warehouse/', include('LogiSolutions.warehouse.urls'),
         )

]
