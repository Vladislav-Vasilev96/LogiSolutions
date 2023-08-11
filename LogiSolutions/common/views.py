from django.views import generic as generic_views

from LogiSolutions.accounts.models import Profile
from LogiSolutions.cargo.models import Cargo
from LogiSolutions.vehicle.models import Vehicle
from LogiSolutions.warehouse.models import Warehouse


class IndexView(generic_views.TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user


        # try:
        #     profile = Profile.objects.get(user=user.pk)
        #     context['profile'] = profile
        # except Profile.DoesNotExist:
        #     context['profile'] = None
        # context['user'] = user
        # return context



class CargoCatalog(generic_views.ListView):
    template_name = 'common/cargo-catalog.html'

    def get_queryset(self):
        return Cargo.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargos'] = Cargo.objects.all().order_by('-created_at')
        return context


class VehicleCatalog(generic_views.ListView):
    template_name = 'common/vehicle-catalog.html'

    def get_queryset(self):
        return Vehicle.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicles'] = Vehicle.objects.all().order_by('-created_at')
        return context


class WarehouseCatalog(generic_views.ListView):
    template_name = 'common/warehouse-catalog.html'

    def get_queryset(self):
        return Warehouse.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['warehouses'] = Warehouse.objects.all().order_by('-created_at')
        return contex


