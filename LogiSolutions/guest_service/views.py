from django.shortcuts import render
from django.views import generic as generic_views


class GuestUserView(generic_views.TemplateView):
    template_name = 'guest_service/guest-service.html'
