from django.urls import path

from keys.views import (
    KeyListView,
    KeyCreateView,
)

urlpatterns = [
    path("list/", KeyListView.as_view(), name="list_keys"),
    path("create/", KeyCreateView.as_view(), name="create_key"),
]
