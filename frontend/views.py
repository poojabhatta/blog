from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
import requests
import json
from django.views.generic import *
from dashboard.models import Post, Category
from django.db.models import Count, Q
from frontend.models import Passanger


def ticket_class_view(request):
    survived = Passanger.objects.filter(survived=True)
    not_survived = Passanger.objects.filter(survived=False)
    dataset = Passanger.objects.values('ticket_class').annotate(survived_count=Count('ticket_class', survived), not_survived_count=Count('ticket_class', not_survived)).order_by('ticket_class')
    return render(request, 'frontend/chart.html', {'dataset': dataset} )



'''
class EmployerListView(View):
    template_name = 'post_list.html'
    
    def get(self, request, *args, **kwargs):
        try:
            employer = requests.get('http://www.jagirkhulyo.com/api/employer/list/').json()
            count = requests.get('http://www.jagirkhulyo.com/api/home/summary/').json()
        except:
            pass
        return render(request, self.template_name, context={'employers': employer, 'count': count})


        # next_page = r['next']
        # for page in next_page:
        #     p = (page.split('=')[-1])
        #     print(p)
        #     next = requests.get('http://127.0.0.1:8085/api/employer/list/', params={'page': p}).json()
        #     print(next)
        # r = requests.get('http://127.0.0.1:8085/api/employer/list/')
        # employer = None
        # if r.status_code == 200:
        #     employer = json.loads(r.text)            
        # return render(request, self.template_name, context= {'employers':employer})
'''


class IndexView(ListView):
    template_name = "frontend/index.html"
    model = Post
    queryset = Post.objects.all()


class PostListView(ListView):
    queryset = Post.objects.all()
    model = Post
    template_name = 'frontend/index.html'

    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        return context


    