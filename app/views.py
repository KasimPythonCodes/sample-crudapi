from django.shortcuts import render
from app.serializers import StudentSerializers
from app import models
from rest_framework import status,serializers,response ,filters
from rest_framework.generics import GenericAPIView ,ListAPIView

# Create your views here.

class StudentRegistrationsearch(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [filters.SearchFilter]
    search_fields =['email']

class StudentRegistration(GenericAPIView):
    serializer_class = StudentSerializers
    queryset = models.Student.objects.all()

    def get(self,request):
        stu=models.Student.objects.all()
        serializer= self.serializer_class(stu , many=True)
        return response.Response(serializer.data)
    
    def post(self ,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.validated_data.get('email')
        Password=serializer.validated_data.get('Password')
        reg = models.Student(email=email ,Password=Password)
        reg.save()
        msg = 'Your registration created successfully!'
        return response.Response({'msg':msg},status=status.HTTP_201_CREATED)
    
class Studentupdate(GenericAPIView):
    serializer_class = StudentSerializers
    queryset = models.Student.objects.all()
    def get(self,request,id):
        getid = models.Student.objects.get(id=id)
        serializer = self.serializer_class(getid)
        return response.Response(serializer.data)
    
    def put(self,request ,id):
        upid = models.Student.objects.get(id=id)
        serializer = self.serializer_class(upid , data=request.data)
        serializer.is_valid(raise_exception=True)
        email =serializer.validated_data.get('email')
        Password =serializer.validated_data.get('Password')
        upid.email=email
        upid.Password=Password
        upid.save()
        msg = 'Your profile changed successfully!'
        return response.Response({'msg':msg},status=status.HTTP_202_ACCEPTED)
    
    def delete(self,request,id):
        dlid = models.Student.objects.get(id=id)
        dlid.delete()
        msg ='Your profile deleted successfully!'
        return response.Response({'msg':msg},status=status.HTTP_200_OK)
        