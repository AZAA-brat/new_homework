from django.urls import path
from django.views.generic import RedirectView

from .views import NoteCreateView, ProfileView, SignUpView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='profile', permanent=False), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('notes/new/', NoteCreateView.as_view(), name='note_create'),
]
