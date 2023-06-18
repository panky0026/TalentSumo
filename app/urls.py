from django.urls import path, include
from app.views import NoteListCreateView, NoteRetrieveView, SharedNoteCreateView

urlpatterns = [
    path('api/notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('api/notes/<int:pk>/', NoteRetrieveView.as_view(), name='note-retrieve'),
    path('api/notes/share/', SharedNoteCreateView.as_view(), name='note-share'),
]
