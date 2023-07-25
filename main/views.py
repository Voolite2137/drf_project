from rest_framework import views,status
from .models import Animals,Cages, Employees, Positions
from . import serializers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import login,logout
# Create your views here.
class OverallView(views.APIView):
    def get(self,request):
        return Response({
            'animals':reverse('animals', request=request),
            'cages':reverse('cages', request=request),
            'employees':reverse('employees', request=request),
            'positions':reverse('positions',request=request),
            'register':reverse('register',request=request),
            'login':reverse('login',request=request)
            })
    
class AnimalsOvearallView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.AnimalsSerializer
    def get(self,request):
        queryset = Animals.objects.all()
        serializer_class = serializers.AnimalsSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def post(self,request):
        serializer_class = serializers.AnimalsSerializer(data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'message':'Instance Created'})
        else:
            return Response({'message':serializer_class.errors})
        
    def delete(self,request):
        Animals.objects.all().delete()
        return Response({"message":"Animals deleted"})
    
class AnimalsDetailedView(views.APIView):
    def get(self,request,pk):
        queryset = Animals.objects.get(id=pk)
        serializer_class = serializers.AnimalsSerializer(queryset,many=False)
        return Response(serializer_class.data)

    def delete(self,request,id):
        Animals.objects.get(id=id).delete()
        return Response({"message":"Animal deleted"})
    
class CagesOvearallView(views.APIView):
    serializer_class = serializers.CagesSerializer
    def get(self,request):
        queryset = Cages.objects.all()
        serializer_class = serializers.CagesSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def post(self,request):
        serializer_class = serializers.CagesSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'message':'Cage added'})
        else:
            return Response({'message':serializer_class.errors})
        
    def delete(self,request):
        Cages.objects.all().delete()
        return Response({"message":"Cages deleted"})
    
class CagesDetailedView(views.APIView):
    def get(self,request,id):
        queryset = Cages.objects.get(id=id)
        serializer_class = serializers.CagesSerializer(queryset,many=False)
        return Response(serializer_class.data)
    
    def delete(self,request,id):
        Cages.objects.get(id=id).delete()
        return Response({'message':'Cage deleted'})
    
    
    
class EmployeesView(views.APIView):
    serializer_class = serializers.EmployeesSerializer
    def get(self,request):
        queryset = Employees.objects.all()
        serializer_class = serializers.EmployeesSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def post(self,request):
        serializer_class = serializers.EmployeesSerializer(data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'message':"Employee added"})
        else:
            return Response({'message':serializer_class.errors})
    
    def delete(self,request):
        Employees.objects.all().delete()
        return Response({"message":"Employees deleted"})
        
class EmployeesDetailedView(views.APIView):
    def get(self,request,id):
        return Response(serializers.EmployeesSerializer(Employees.objects.get(id=id),many=False).data)
    
    def delete(self,request,id):
        Employees.objects.get(id=id).delete()
        return Response({"message":"Employee deleted"})
    
class PositionsView(views.APIView):
    serializer_class = serializers.PositionsSerializer
    def get(self,request):
        queryset = Positions.objects.all()
        serializer_class = serializers.PositionsSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def post(self,request):
        serializer_class = serializers.PositionsSerializer(data = request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'message':"Position added"})
        else:
            return Response({'message':serializer_class.errors})
    
    def delete(self,request):
        Employees.objects.all().delete()
        return Response({"message":"Positions deleted"})
        
class PositionsDetailedView(views.APIView):
    def get(self,request,id):
        return Response(serializers.PositionsSerializer(Positions.objects.get(id=id),many=False).data)
    
    def delete(self,request,id):
        Positions.objects.get(id=id).delete()
        return Response({"message":"Position deleted"})
    
class RegisterUser(views.APIView):
    serializer_class = serializers.UserRegisterSerializer
    def post(self,request):
        serializer = serializers.UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token':token.key,'user':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginUser(views.APIView):
    def post(self,request):
        user = get_object_or_404(User,username = request.data['username'])
        if not user.check_password(request.data['password']):
            raise Http404
        token = Token.objects.get(user=user)
        login(request,user)
        return Response({"token":token.key})

class LogoutUser(views.APIView):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('main',request=request))
        
