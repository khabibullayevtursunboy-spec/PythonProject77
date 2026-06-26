from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.shortcuts import render
from .models import Maqola


class MaqolaList(LoginRequiredMixin, ListView):
    model = Maqola
    template_name = 'royxat.html'
    context_object_name = 'maqolalar'
    paginate_by = 5

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        sort = self.request.GET.get('sort', '-sana')  # ← yangi

        # Faqat ruxsat etilgan maydonlar bo'yicha saralash (xavfsizlik uchun)
        allowed_sorts = ['sarlavha', '-sarlavha', 'sana', '-sana', 'muallif', '-muallif']
        if sort not in allowed_sorts:
            sort = '-sana'

        maqolalar = Maqola.objects.filter(chop_etilgan=True).order_by(sort)
        if q:
            maqolalar = maqolalar.filter(
                Q(sarlavha__icontains=q) |
                Q(muallif__icontains=q)
            )
        return maqolalar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jami'] = Maqola.objects.count()
        context['sarlavha'] = 'Barcha maqolalar'
        context['q'] = self.request.GET.get('q', '')
        context['sort'] = self.request.GET.get('sort', '-sana')  # ← yangi
        return context


class MaqolaDetail(LoginRequiredMixin, DetailView):
    model = Maqola
    template_name = 'detail.html'
    context_object_name = 'maqola'


class MaqolaCreate(LoginRequiredMixin, CreateView):
    model = Maqola
    template_name = 'maqola_form.html'
    fields = ['sarlavha', 'muallif', 'matn', 'chop_etilgan']
    success_url = reverse_lazy('royxat')


class MaqolaUpdate(LoginRequiredMixin, UpdateView):
    model = Maqola
    template_name = 'maqola_form.html'
    fields = ['sarlavha', 'muallif', 'matn', 'chop_etilgan']
    success_url = reverse_lazy('royxat')


class MaqolaDelete(LoginRequiredMixin, DeleteView):
    model = Maqola
    template_name = 'maqola_confirm_delete.html'
    success_url = reverse_lazy('royxat')


class BizHaqimizda(TemplateView):
    template_name = 'about.html'


class EskiBlog(RedirectView):
    pattern_name = 'royxat'