from django.conf.urls import url
from .views import *

app_name = 'frontend'

urlpatterns = [

    url(r'^$', IndexView.as_view(), name = 'index_view'),
    url(r'^post/(?P<pk>\d+)/detail', PostDetailView.as_view(), name='post_detail'),
    # url(r'^chart$', ticket_class_view, name='chart_js'),

]