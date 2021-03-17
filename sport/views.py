from django.shortcuts import render
from .models import Sports
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class SportsListView(ListView):
    model = Sports
    template_name = 'sport/home.html'
    context_object_name = 'trainings'

class SportsCreateView(CreateView):
    model = Sports
    fields = ['sport', 'duration', 'feedback']
    success_url = '/'

class SportsUpdateView(UpdateView):
    model = Sports
    fields = ['sport', 'duration', 'feedback']
    success_url = '/'

class SportsDeleteView(DeleteView):
    model = Sports
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)