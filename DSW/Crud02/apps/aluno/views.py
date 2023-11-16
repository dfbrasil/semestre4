from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy


from .models import Aluno

class AlunoList(ListView):
    model = Aluno

class AlunoDetail(DetailView):
    model = Aluno
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["now"] = timezone.now()
        return context
    
class AlunoCreate(CreateView):
    model = Aluno
    fields = '__all__'
    success_url = 'aluno_list'
    
class AlunoUpdate(UpdateView):
    model = Aluno
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('aluno_list')
    
class AlunoDelete(DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno_list')