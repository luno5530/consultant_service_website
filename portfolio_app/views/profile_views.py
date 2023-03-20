from typing import Any
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from ..models import Profile, CurriculumVitae, CurriculumVitaSection

class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'portfolio_app/profile_details.html'
    
    def get_object(self):
        return get_object_or_404(self.model, pk=1)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object()
        context['cvs_list'] = get_object_or_404(CurriculumVitae, pk=self.get_object()).curriculumvitasection_set.all()
        return context

