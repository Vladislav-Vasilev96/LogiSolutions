from django.urls import reverse_lazy
from django.views import generic as generic_views

from LogiSolutions.warehouse.forms import WarehouseForm


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


class DetailsWarehouseView(generic_views.DetailView):
    template_name = 'warehouse/details-warehouse.html'


class DeleteWarehouseView(generic_views.DeleteView):
    template_name = 'warehouse/delete-warehouse.html'
    success_url = reverse_lazy('index')
