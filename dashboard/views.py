from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse
from .mixins import *
from .utils import post_scrapping

# class IndexView(TemplateView):
#     template_name = 'dashboard/account/index.html'

class HomeView(LoginRequired404Mixin,TemplateView):
    template_name = 'dashboard/account/home.html'


class LoginView(View):
    form_class = LoginForm

    def get(self, *args, **kwargs):
        form = LoginForm()
        return render(self.request, 'dashboard/account/index.html', {'form': form})

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            print(username, password,44444444)
            user = authenticate(self.request, username=username, password=password)
            print(user)
            if user:
                login(self.request, user)
                return HttpResponseRedirect(reverse('dashboard:home'))
            else:
                return HttpResponse('Username and Password invalid')
                pass
        else:
            pass

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('dashboard:login'))


class PostCreateView(LoginRequired404Mixin,CreateView):
    template_name =  'dashboard/post/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('dashboard:home')

    # def form_valid(self, form):
        # url = form.cleaned_data.get('url')
        # post_scrapping(url)
        # return super().form_valid(form)
    

# class PostListView(LoginRequired404Mixin,ListView):
#     template_name = 'dashboard/post/post_list.html'
#     queryset = Post.objects.all()
    
