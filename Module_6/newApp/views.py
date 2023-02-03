from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import BookSerializer
from rest_framework.renderers import JSONRenderer

# single book data
def book_details(request, pk):
    book= Book.objects.get(id=pk)
    serializer= BookSerializer(book)
    json_data= JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type='application/json')

#  query set- all book data
def book_list(request):
    book= Book.objects.all()
    serializer= BookSerializer(book,many=True)
    json_data= JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type='application/json')