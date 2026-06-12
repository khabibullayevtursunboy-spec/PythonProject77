from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Maqola

class MaqolaList(ListView):
    model = Maqola
    template_name = 'royxat.html'
    context_object_name = 'maqolalar'

    def get_queryset(self):
        return Maqola.objects.filter(chop_etilgan=True).order_by('-sana')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jami'] = Maqola.objects.count()
        context['sarlavha'] = 'Barcha maqolalar'
        return context

class MaqolaDetail(DetailView):
    model = Maqola
    template_name = 'detail.html'
    context_object_name = 'maqola'

class MaqolaCreate(CreateView):
    model = Maqola
    template_name = 'maqola_form.html'
    fields = ['sarlavha', 'muallif', 'matn', 'chop_etilgan']
    success_url = reverse_lazy('royxat')

class MaqolaUpdate(UpdateView):
    model = Maqola
    template_name = 'maqola_form.html'
    fields = ['sarlavha', 'muallif', 'matn', 'chop_etilgan']
    success_url = reverse_lazy('royxat')

class MaqolaDelete(DeleteView):
    model = Maqola
    template_name = 'maqola_confirm_delete.html'
    success_url = reverse_lazy('royxat')

class BizHaqimizda(TemplateView):
    template_name = 'about.html'

class EskiBlog(RedirectView):
    pattern_name = 'royxat'