from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project

# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ["name", "description", "members"]
    success_url = reverse_lazy("show_project")

    # very unsure about part below. Wasn't sure how to
    # assign item.members = self.request.user

    def form_valid(self, form):
        item = form.save(commit=False)
        item.auth_User = self.request.user
        item.save()
        form.save_m2m()
        return redirect("show_project", pk=item.id)
