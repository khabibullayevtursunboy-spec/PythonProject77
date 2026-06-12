from django.urls import path
from .views import (
    MaqolaList, MaqolaDetail, MaqolaCreate,
    MaqolaUpdate, MaqolaDelete, BizHaqimizda, EskiBlog
)

urlpatterns = [
    path('', MaqolaList.as_view(), name='royxat'),
    path('yangi/', MaqolaCreate.as_view(), name='maqola_yangi'),
    path('<int:pk>/', MaqolaDetail.as_view(), name='detail'),
    path('<int:pk>/tahrirlash/', MaqolaUpdate.as_view(), name='maqola_tahrirlash'),
    path('<int:pk>/ochirish/', MaqolaDelete.as_view(), name='maqola_ochirish'),
    path('about/', BizHaqimizda.as_view(), name='about'),
    path('eski-blog/', EskiBlog.as_view(), name='eski-blog'),
]