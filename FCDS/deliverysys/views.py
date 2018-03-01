"""This is core file to keep track on delivery of products."""
# from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView)
# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = ['Pradam', 'Abhilash']
        return context


class HuskListPage(TemplateView):
    template_name = "husks_list.html"


class HuskAddPage(TemplateView):
    template_name = "husk_add.html"


class CoalPageList(TemplateView):
    template_name = "coal_list.html"
