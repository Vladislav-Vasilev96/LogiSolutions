from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as generic_views

from LogiSolutions.cargo.forms import CargoForm
from LogiSolutions.cargo.models import Cargo


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
    form_class = CargoForm
    model = Cargo


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cargo = self.get_object()
        context['cargo'] = cargo
        return context

    def get_success_url(self):
        pk = self.object.pk
        return reverse('details cargo', kwargs={'pk': pk})


class DetailsCargoView(generic_views.DetailView):
    template_name = 'cargo/details-cargo.html'
    model = Cargo
    form_class = CargoForm

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:  # If the user is not an admin, filter by is_approved=True
            queryset = queryset.filter(is_approved=True)
        return queryset

class DeleteCargoView(generic_views.DeleteView):
    template_name = 'cargo/delete-cargo.html'
    model = Cargo
    success_url = reverse_lazy('IndexView')

    def get_success_url(self):
        if 'next' in self.request.POST:
            return self.request.POST['next']
        return self.success_url

    def delete(self, request, *args, **kwargs):
        self.object.delete()
        return redirect(self.get_success_url())


def approve_cargo(request, pk):
    cargo = Cargo.objects.get(pk=pk)
    cargo.is_approved = True
    cargo.save()
    return redirect('admin:cargo_cargo_changelist')