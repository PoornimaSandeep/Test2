from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework import serializers
from .serializers import Article_serializer
from .models import Article

@csrf_exempt
def article_list(request):
    if request.method=='GET':
       articles=Article.objects.all()
       serial=Article_serializer(articles,many=True)
       return JsonResponse(serial.data,safe=False)

    elif request.method=='POST':
         data=JSONParser().parse(request)
         serializer=Article_serializer(data=data)

         if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
         else:
             return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def article_details(request,pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
          return HttpResponse(status=404)

    if request.method=='GET':
        serializers=Article_serializer(article)
        return JsonResponse(serializers.data)

    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializers=Article_serializer(article,data=data)

        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data,status=201)
        return JsonResponse(serializers.errors,status=400)

    elif request.method=='DELETE':
         article.delete()
         return HttpResponse(status=204)












