from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views
from LogiSolutions.accounts.forms import RegisterUserForm, ChangePasswordForm
from LogiSolutions.accounts.models import CustomUser, Profile

UserModel = get_user_model()


class CustomPermissionMixin(generic_views.View):
    def dispatch(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=kwargs['pk'])
        if request.user != user:
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(generic_views.CreateView):
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('IndexView')
    form_class = RegisterUserForm

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context


class LoginUserView(LoginView):
    template_name = 'profiles/login.html'

    def get_success_url(self):
        return reverse_lazy('IndexView')


# class LoginUserView(LoginView):
#     redirect_authenticated_user = True
#     template_name = 'profiles/login.html'
#     success_url = reverse_lazy('IndexView')
#
#
#     def get_success_url(self):
#         if self.success_url:
#             return self.success_url
#         return super().success_url

class LogoutConfirmationView(generic_views.TemplateView):
    template_name = 'profiles/logout-confromation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_url'] = reverse_lazy('LogoutView')
        return context


class LogoutUserView(LogoutView):
    template_name = 'profiles/logout.html'
    # next_page = reverse_lazy('IndexView')


class DetailUserView(generic_views.DetailView):
    TEMPLATE_NAME = 'Profile Details'
    model = Profile
    template_name = 'profiles/details-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        profile = Profile.objects.get(pk=user.id)
        context['profile'] = profile
        context['user'] = user
        context['template_name'] = self.TEMPLATE_NAME
        return context

class EditUserView(generic_views.UpdateView):
    TEMPLATE_NAME = 'Edit Profile'
    model = Profile
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('IndexView')
    fields = ('profile_image', 'first_name', 'last_name',)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


class DeleteUserView(CustomPermissionMixin, generic_views.DeleteView):
    TEMPLATE_NAME = 'Delete Profile'
    model = CustomUser
    success_url = reverse_lazy('IndexView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


class ChangePasswordView(CustomPermissionMixin, generic_views.UpdateView):
    TEMPLATE_NAME = 'Change Password'
    model = Profile
    form_clas = ChangePasswordForm
    fields = '__all__'
    template_name = 'profiles/change-password.html'

    def get_form_class(self):
        return self.form_clas

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs.pop('instance')
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


