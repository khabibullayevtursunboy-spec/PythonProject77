from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from .models import Maqola

class MaqolaListView(ListView):
    model = Maqola
    template_name = 'blog/maqola_list.html'
    context_object_name = 'maqolalar'

    def get_queryset(self):
        return Maqola.objects.filter(chop_etilgan=True).order_by('-sana')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jami_maqolalar'] = Maqola.objects.count()
        return context

class MaqolaDetailView(DetailView):
    model = Maqola
    template_name = 'blog/maqola_detail.html'
    context_object_name = 'maqola'

class BizHaqimizdaView(TemplateView):
    template_name = 'blog/biz_haqimizda.html'

class EskiHavolaRedirectView(RedirectView):
    pattern_name = 'maqola_list'