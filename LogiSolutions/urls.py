from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('LogiSolutions.accounts')),
    path('photos/', include('LogiSolutions.photos')),
    path('common/', include('LogiSolutions.common')),

]
