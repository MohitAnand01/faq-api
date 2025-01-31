from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

@api_view(["GET"])
def faq_list(request):
    lang = request.GET.get("lang", "en")
    cache_key = f"faqs_{lang}"

    if cache_key in cache:
        faqs = cache.get(cache_key)
    else:
        faqs = FAQ.objects.all()
        for faq in faqs:
            faq.question = faq.get_translated_question(lang)
        faqs = FAQSerializer(faqs, many=True).data
        cache.set(cache_key, faqs, timeout=3600)

    return Response(faqs)

