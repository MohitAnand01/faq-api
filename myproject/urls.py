from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the FAQ API! Use /api/faqs/ to get FAQs."})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/faqs/', include('faqs.urls')),  # API routes
    path('', home),  # Set homepage route
]

