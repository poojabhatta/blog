from django.conf.urls import url
from .views import *

app_name = 'frontend'

urlpatterns = [

    url(r'^$', IndexView.as_view(), name = 'index_view'),
    # url(r'^chart$', ticket_class_view, name='chart_js'),

]