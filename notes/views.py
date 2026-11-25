from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import SignUpForm
from .models import Note


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(author=self.request.user)
        return context


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ('title', 'content')
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        self.object = obj
        return redirect(self.get_success_url())
