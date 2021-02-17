from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Farm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse


# Create your views here.
class FarmListView(LoginRequiredMixin, ListView):
    model = Farm

    # Template_Name : <app>/<model>_<viewtype>.html
    def get_queryset(self):
        return Farm.objects.filter(owner=self.request.user)


class FarmDetailView(LoginRequiredMixin, DetailView):
    model = Farm


class FarmCreateView(LoginRequiredMixin, CreateView):
    model = Farm
    fields = ['state', 'village', 'total_land_available', 'land_cultivating', 'crop', 'expecting_yield', 'water_source']
    success_url = '/user/farm/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class FarmUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Farm
    fields = ['state', 'village', 'total_land_available', 'land_cultivating', 'crop', 'expecting_yield', 'water_source']
    success_url = '/user/farm/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        farm = self.get_object()
        return farm.owner == self.request.user


class FarmDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Farm
    success_url = '/user/farm'

    def test_func(self):
        farm = self.get_object()
        return farm.owner == self.request.user

