from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from .serializers import UserSer,TodoSer
from.models import TodoModel
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
# Create your views here.

class SignUpViewSet(ViewSet):
    def create(self,request):
        ser=UserSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Success"})
        return Response({"msg":"Failed"})            
    
class TodoMViewSet(ModelViewSet):
    serializer_class = TodoSer
    queryset = TodoModel.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        ser=TodoSer(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response({"msg":"Todo Added"})
        return Response({"msg":"Failed"})
    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)