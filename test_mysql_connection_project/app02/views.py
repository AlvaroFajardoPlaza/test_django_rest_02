from django.shortcuts import render
from .models import TestModel01
from .serializers import TestModel01Serializer

# Importamos el modulo para poder manejar respuesta de tipo JSON
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

# 1º función para retornar toda la data de la app
@api_view(['GET'])
def get_all_data(request):
    data = TestModel01.objects.all()
    #print("Mandamos la data?", data) # Recibimos bien la data, pero hay que transformarla a Json
    serializer = TestModel01Serializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_new_character(request):
    if request.method == 'POST':
        serializer = TestModel01Serializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print("form is not valid")
            return Response(serializer.errors, status=400)



