from django.urls import path

from .views import NoteListCreateView, NoteRetriveUpdateDeleteView

app_name = "note"

urlpatterns = [
    path("note/", NoteListCreateView.as_view(), name="note-list"),
    path("note/create", NoteListCreateView.as_view(), name="note-create"),
    path("note/<int:pk>/", NoteRetriveUpdateDeleteView.as_view(), name="note-detail"),
    path(
        "note/<int:pk>/update",
        NoteRetriveUpdateDeleteView.as_view(),
        name="note-update",
    ),
    path(
        "note/<int:pk>/delete",
        NoteRetriveUpdateDeleteView.as_view(),
        name="note-delete",
    ),
]
