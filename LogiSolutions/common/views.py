from django.shortcuts import render
from django.views import generic as generic_views


class IndexView(generic_views.TemplateView):
    template_name = 'common/index.html'


class CatalogView(generic_views.ListView):
    TEMPlATE_NAME = 'catalog'
    template_name = 'common/catalogue.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPlATE_NAME
        # context['object_list'] =
        # context['object_list'] = Review.objects.filter(is_approved=Review.APPROVED)
        return context

