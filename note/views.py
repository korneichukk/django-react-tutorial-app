from rest_framework import generics

from .models import Note
from .serializers import NoteSerializer


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by("-updated")
    serializer_class = NoteSerializer


class NoteRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all().order_by("-updated")
    serializer_class = NoteSerializer
