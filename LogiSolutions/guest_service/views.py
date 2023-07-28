from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_views

from LogiSolutions.guest_service.forms import QuestionForm
from LogiSolutions.guest_service.models import GuestServiceFormSubmission


class AskQuestionView(generic_views.FormView):
    template_name = 'guest_service/guest-service.html'
    form_class = QuestionForm
    success_url = reverse_lazy('IndexView')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = GuestServiceFormSubmission.objects.all()
        return context