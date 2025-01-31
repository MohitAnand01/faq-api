from django.urls import path
from .views import faq_list, faq_detail

urlpatterns = [
    path('', faq_list, name='faq-list'),  # ✅ GET & POST
    path('<int:pk>/', faq_detail, name='faq-detail'),  # ✅ GET, PUT & DELETE for specific FAQ
]
