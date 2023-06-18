from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Note, SharedNote
from .serializers import NoteSerializer, SharedNoteSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NoteRetrieveView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

class SharedNoteCreateView(generics.CreateAPIView):
    queryset = SharedNote.objects.all()
    serializer_class = SharedNoteSerializer
    permission_classes = [IsAuthenticated]
