from django.shortcuts import render
from django.views import generic as generic_views


class IndexView(generic_views.TemplateView):
    template_name = 'common/index.html'


class CatalogView(generic_views.ListView):
    template_name = 'common/catalogue.html'

