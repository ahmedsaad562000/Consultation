
from django.shortcuts import render
import pprint

from django.contrib.auth import authenticate

from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
# Create your views here.
from .serializers import Add_User_Serializer, UserSerializer , NO_Verify_UserSerializer
from accounts.models import User as userview
from django.db.models import Q

from rest_framework import status

from api import approve, serializers


@api_view(['GET','POST'])
def apiOverview(request):
	api_urls = {
        'Users':'-----------------------------------------',
		'Approve User':'http://localhost:8000/api/approve/<str:name>/',
		'Get User':'http://localhost:8000/api/getuser/<str:name>/',
		'ADD User':'http://localhost:8000/api/adduser/',
		'Update User':'http://localhost:8000/api/updateuser/<str:name>/',
		'Delete User':'http://localhost:8000/api/deleteuser/<str:name>/',
        'login' : 'http://localhost:8000/api/login/<str:name>&<str:password>',
        'All Users List':'http://localhost:8000/api/users',
        'Approved Users List':'http://localhost:8000/api/appusers/',
        'Unapproved Users List':'http://localhost:8000/api/unappusers/',
		'Stadiums':'----------------------------------------',
        'Add New Stadium':'http://localhost:8000/api/addstadium/',
        'Get All Stadiums':'http://localhost:8000/api/stadiums/',
        'Matches':'----------------------------------------',
        'Get All Matches':'http://localhost:8000/api/matches/',
        'Add Match':'http://localhost:8000/api/addmatch/',
        'Update Match':'http://localhost:8000/api/updatematch/<int:match_id>/',
        'Teams':'----------------------------------------',
        'Get All Teams':'http://localhost:8000/api/teams',
        'Refrees':'----------------------------------------',
        'Get All Refrees':'http://localhost:8000/api/refs',
        'Tickets':'----------------------------------------',
        'Get Tickets of a user':'http://localhost:8000/api/tickets/<str:name>/',
        'Delete Ticket':'http://localhost:8000/api/deleteticket/<int:ticketid>/',
        'Add Ticket':'http://localhost:8000/api/addticket/<str:username>/',
        'Get seats of a match':'http://localhost:8000/api/seats/<int:match_id>/'
        }

	return Response(api_urls)



@api_view(['GET'])
def UserList(request):
    users = userview.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def GetUser(request, name):
    try:
        users = userview.objects.get(username=name)
        serializer = UserSerializer(users, many=False)
        return Response(serializer.data)
    except userview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def approveUser(request, name):
    try:
        user = userview.objects.get(username=name)
        user.approved=True;
        user.save();
        return Response(status=status.HTTP_200_OK)
    except userview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def AddUser(request):
    serializer = Add_User_Serializer(data=request.data)
    
    if serializer.is_valid():
            serializer.save();
            return Response(status=status.HTTP_200_OK);

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST);



@api_view(['POST'])
def UpdateUser(request , name):
    try:
        user = userview.objects.get(username=name)
    except userview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND);
    serializer = NO_Verify_UserSerializer(instance=user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK);
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST);



@api_view(['DELETE'])
def DeleteUser(request , name):
    try:
        user = userview.objects.get(username=name)
    except userview.DoesNotExist: 
        return Response(status=status.HTTP_400_BAD_REQUEST)    
    user.delete()
    return Response(status=status.HTTP_200_OK)



@api_view(['GET' , 'POST'])
def login(request , name , password):
    
        user = authenticate(username=name , password=password)
        if user is not None:
            if user.role=='A' or user.approved==True:
               # login(request, user);
                pp = pprint.PrettyPrinter(indent=4)
                pp.pprint("You are now logged in as "+user.username+ " with role: "+user.role)
                
                return Response({
                    "id" : user.id,
                    "username" : user.username,
                    "role" : user.role
                });
            elif user.approves==False:
                return Response(status=status.HTTP_401_UNAUTHORIZED);    
        else:
            return Response(status=status.HTTP_403_FORBIDDEN);

@api_view(['GET'])
def ApprovedUserList(request):
    users = userview.objects.filter(Q(approved=True) , Q(role='F') | Q(role='M') )
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UnapprovedUserList(request):
    users = userview.objects.filter(Q(approved=False) , Q(role='F') | Q(role='M') )
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


