from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from keys.models import Key

# Create your views here.
class KeyListView(LoginRequiredMixin, ListView):
    model = Key
    template_name = "keys/list.html"

    def get_queryset(self):
        return Key.objects.filter(assignee=self.request.user)
