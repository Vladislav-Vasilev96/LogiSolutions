from django.urls import reverse_lazy
from django.views import generic as generic_views

from LogiSolutions.cargo.forms import CargoForm



class CreateCargoView(generic_views.CreateView):
    template_name = 'cargo/add-cargo.html'
    success_url = reverse_lazy('IndexView')
    form_class = CargoForm

    def form_valid(self, form):
        if form.is_valid():
            form.instance.owner = self.request.user
            return super().form_valid(form)


class EditCargoView(generic_views.UpdateView):
    template_name = 'cargo/edit-cargo.html'

class DetailsCargoView(generic_views.DetailView):
    template_name = 'cargo/details-cargo.html'
class DeleteCargoView(generic_views.DeleteView):
    template_name = 'cargo/delete-cargo.html'
