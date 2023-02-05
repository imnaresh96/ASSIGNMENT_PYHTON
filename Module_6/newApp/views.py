from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializers import BookSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



# # single book data
def book_details(request, pk):
    book= Book.objects.get(id=pk)
    serializer= BookSerializer(book)
    # json_data= JSONRenderer().render(serializer.data)
    
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)


#  query set- all book data
def book_list(request):
    book= Book.objects.all()
    serializer= BookSerializer(book,many=True)
    json_data= JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data, safe=False)

# create/insert data  
@csrf_exempt
def book_create(request):
    if request.method =='POST':
        json_data = request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=BookSerializer(data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
            # return JsonResponse(serializer.data, safe=False)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
        # return JsonResponse(serializer.data, safe=False)
    
def book_update(request):
    if request.method =='GET':
        json_data= request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            book_data=Book.objects.get(id=id)
            serializer=BookSerializer(data=book_data)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        book=Book.objects.all()
        serializer=BookSerializer(book, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
         