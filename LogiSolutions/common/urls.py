from django.urls import path

from LogiSolutions.common.views import IndexView, CatalogView

urlpatterns = (
    path('', IndexView.as_view(), name='IndexView'),
    path('catalog/', CatalogView.as_view(), name='CatalogView')
)
