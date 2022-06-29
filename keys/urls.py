from django.urls import path

from keys.views import KeyListView, KeyCreateView, KeyDeleteView

urlpatterns = [
    path("list/", KeyListView.as_view(), name="list_keys"),
    path("create/", KeyCreateView.as_view(), name="create_key"),
    path("<int:pk>/delete/", KeyDeleteView.as_view(), name="delete_key")
]
