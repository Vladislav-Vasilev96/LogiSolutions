from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as generic_views

from LogiSolutions.warehouse.forms import WarehouseForm
from LogiSolutions.warehouse.models import Warehouse


class CreateWarehouseView(generic_views.CreateView):
    template_name = 'warehouse/add-warehouse.html'
    success_url = reverse_lazy('IndexView')
    form_class = WarehouseForm

    def form_valid(self, form):
        if form.is_valid():
            form.instance.owner = self.request.user
            return super().form_valid(form)


class EditWarehouseView(generic_views.UpdateView):
    template_name = 'warehouse/edit-warehouse.html'
    form_class = WarehouseForm
    model = Warehouse

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.owner
        warehouse = Warehouse.objects.get(pk=user.id)
        context['warehouse'] = warehouse
        return context

    def get_success_url(self):
        pk = self.object.pk
        return reverse('details vehicle', kwargs={'pk': pk})


class DetailsWarehouseView(generic_views.DetailView):
    template_name = 'warehouse/details-warehouse.html'
    model = Warehouse
    form_class = WarehouseForm


class DeleteWarehouseView(generic_views.DeleteView):
    template_name = 'warehouse/delete-warehouse.html'
    success_url = reverse_lazy('IndexView')
    model = Warehouse

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url

    def delete(self, request, *args, **kwargs):
        self.object.delete()
        return redirect(self.get_success_url())
