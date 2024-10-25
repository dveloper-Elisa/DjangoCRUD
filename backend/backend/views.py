from django.http import JsonResponse
from .models import Users
from .serializers import BackendSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def getUsers (request):

    if request.method == 'GET' :
        users = Users.objects.all()
        serializer = BackendSerializers(users, many=True)
        return JsonResponse({"users": serializer.data})
    

    if request.method == 'POST' :
        serializer = BackendSerializers(data = request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def userDetails(request, id) :

    try :
        user = Users.objects.get(pk = id)
    except Users.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET' :
        serializer = BackendSerializers(user)
        return Response(serializer.data)
    
    if request.method == 'PUT' :
        serializer = BackendSerializers(user, data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return JsonResponse({"message":"User Updated", "user": serializer.data})
        else :
            return JsonResponse({"message": "User not Updated"}) 
    

    if request.method == "DELETE" :
        user.delete()
        return JsonResponse({"message": "User Deleted", "status" : status.HTTP_205_RESET_CONTENT})