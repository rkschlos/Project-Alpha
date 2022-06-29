from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from keys.models import Key


# Create your views here.


class KeyListView(LoginRequiredMixin, ListView):
    model = Key
    template_name = "keys/list.html"
    # extra_context = {"key": "A"}  # method call to def random

    def get_queryset(self):
        return Key.objects.filter(assignee=self.request.user)

    # #def random_key(request):
    #     my_list = [
    #         "A",
    #         "A#",
    #         "B-flat",
    #         "B",
    #         "C",
    #         "C#",
    #         "D-flat",
    #         "D",
    #         "D#",
    #         "E-flat",
    #         "E",
    #         "F",
    #         "F#",
    #         "G",
    #     ]
    #     rand_key = random.choice(my_list)
    #     html = "<b>Not sure? Random Key:</b> %s" % rand_key
    #     return render(request, html)  # add context


class KeyCreateView(LoginRequiredMixin, CreateView):
    model = Key
    template_name = "keys/create.html"
    fields = [
        "name",
        "date",
        "tempo",
        "notes",
    ]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.assignee = self.request.user
        item.save()
        return redirect("list_keys")


class KeyDeleteView(LoginRequiredMixin, DeleteView):
    model = Key
    template_name = "keys/delete.html"
    success_url = reverse_lazy("list_keys")
