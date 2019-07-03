from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.encoding import force_text
from django.urls import reverse_lazy


class LoginRequired404Mixin(LoginRequiredMixin):
    login_url = reverse_lazy('dashboard:login')

    def get_login_url(self):
        print(555555555555555)
        return force_text(self.login_url)

    def dispatch(self, request, *args, **kwargs):
        if not request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

