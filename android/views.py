from django.shortcuts import render
# from app.models import FPO
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import FpoSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@api_view(['GET','POST'])
@csrf_exempt
def fpolist(request):
    if request.method =="GET":
        pass
        # fpo = FPO.objects.all()
        # se = FpoSerializer(fpo, many=True)
        # # return JsonResponse(se.data, safe=False)
        # # return JsonResponse(se.data, safe=False)
        # return Response(se.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = FpoSerializer(data=request.data)
        print('*'*1000)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print('%'*100)
            print('done')
            return JsonResponse(serializer.data, status=201)
        else:
            print('ser error',serializer.errors)
        return JsonResponse(serializer.errors, status=400)
