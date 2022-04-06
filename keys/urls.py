from django.urls import path

from keys.views import (
    KeyListView,
)

urlpatterns = [path("list/", KeyListView.as_view(), name="list_keys")]
