from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Task


# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = [
        "name",
        "goal_time",
        "project",
    ]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.assignee = self.request.user
        item.save()
        return redirect("show_project", pk=item.project.id)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/mine.html"
    fields = [
        "is_completed",
    ]
    success_url = reverse_lazy("show_my_tasks")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/mine.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("show_my_tasks")
