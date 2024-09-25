from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView


class LoginUser(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self):
        print(self.request.user.is_staff)
        return reverse_lazy('activities:main')

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)


def logout_user(request):
    logout(request)
    return redirect('users:login')
