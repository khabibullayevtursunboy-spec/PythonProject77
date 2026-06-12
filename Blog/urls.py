from django.urls import path
from .views import MaqolaListView, MaqolaDetailView, BizHaqimizdaView, EskiHavolaRedirectView

urlpatterns = [
    path('', MaqolaListView.as_view(), name='maqola_list'),
    path('<int:pk>/', MaqolaDetailView.as_view(), name='maqola_detail'),
    path('biz-haqimizda/', BizHaqimizdaView.as_view(), name='biz_haqimizda'),
    path('eski-url/', EskiHavolaRedirectView.as_view(), name='eski_havola_redirect'),
]