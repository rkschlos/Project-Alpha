from django.urls import path

from projects.views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectDeleteView, 
    metronome,
)


urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
    path("create/", ProjectCreateView.as_view(), name="create_project"),
    path("metronome/", metronome, name="metronome"),
    path("<int:pk>/delete/", ProjectDeleteView.as_view(), name="delete_project")
]
