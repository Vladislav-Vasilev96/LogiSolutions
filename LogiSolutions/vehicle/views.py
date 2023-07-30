from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as generic_views

from LogiSolutions.vehicle.forms import VehicleForm
from LogiSolutions.vehicle.models import Vehicle


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
    form_class = VehicleForm
    model = Vehicle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = self.get_object()
        context['vehicle'] = vehicle
        return context

    def get_success_url(self):
        pk = self.object.pk
        return reverse('details vehicle', kwargs={'pk': pk})


class DetailsVehicleView(generic_views.DetailView):
    template_name = 'vehicle/details-vehicle.html'
    model = Vehicle
    form_class = VehicleForm

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_approved=True)
        return queryset


class DeleteVehicleView(generic_views.DeleteView):
    template_name = 'vehicle/delete-vehicle.html'
    success_url = reverse_lazy('IndexView')
    model = Vehicle

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url

    def delete(self, request, *args, **kwargs):
        self.object.delete()
        return redirect(self.get_success_url())


def approve_vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    vehicle.is_approved = True
    vehicle.save()
    return redirect('admin:vehicle_vehicle_changelist')
