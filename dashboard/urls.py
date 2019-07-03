from django.conf.urls import url
from .views import *

app_name = 'dashboard'

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home$', HomeView.as_view(), name = 'home'),
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^post/create/$', PostCreateView.as_view(), name='post_create'),
    # url(r'^post/list/$', PostListView.as_view(), name='post_create'),
    
]