
from django.urls import reverse_lazy
from django.views import generic as generic_views

from LogiSolutions.vehicle.forms import VehicleForm



class CreateVehicleView(generic_views.CreateView):
    template_name = 'vehicle/add-vehicle.html'
    success_url = reverse_lazy('IndexView')
    form_class = VehicleForm


    def form_valid(self, form):
        if form.is_valid():
            form.instance.owner = self.request.user
            return super().form_valid(form)




class EditVehicleView(generic_views.UpdateView):
    template_name = 'vehicle/edit-vehicle.html'


class DetailsVehicleView(generic_views.DetailView):
    template_name = 'vehicle/details-vehicle.html'


class DeleteVehicleView(generic_views.DeleteView):
    template_name = 'vehicle/delete-vehicle.html'
    success_url = reverse_lazy('index')
