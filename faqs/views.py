from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

@api_view(["GET", "POST"])
def faq_list(request):
    if request.method == "GET":
        lang = request.GET.get("lang", "en")  # Get language from query, default to English
        faqs = FAQ.objects.all()  # Fetch all FAQs

        serialized_data = []
        for faq in faqs:
            data = FAQSerializer(faq).data
            if lang == "hi":
                data["question"] = faq.question_hi or faq.question  # Fallback to English
            elif lang == "bn":
                data["question"] = faq.question_bn or faq.question  # Fallback to English
            serialized_data.append(data)

        return Response(serialized_data, status=status.HTTP_200_OK)  # Return JSON
    
    if request.method == "POST":
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save to database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def faq_detail(request, pk):
    try:
        faq = FAQ.objects.get(pk=pk)
    except FAQ.DoesNotExist:
        return Response({"error": "FAQ not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        lang = request.GET.get("lang", "en")
        serializer = FAQSerializer(faq)
        data = serializer.data

        # Modify question based on the requested language
        if lang == "hi":
            data["question"] = faq.question_hi or faq.question  # Fallback to English
        elif lang == "bn":
            data["question"] = faq.question_bn or faq.question  # Fallback to English

        return Response(data)

    elif request.method == "PUT":
        serializer = FAQSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        faq.delete()
        return Response({"message": "FAQ deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
