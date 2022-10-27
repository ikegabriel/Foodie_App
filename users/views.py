from django.shortcuts import render
from rest_framework.authentication import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.views import csrf_exempt, APIView
from rest_framework import permissions
from rest_framework.response import Response

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib.auth import get_user_model

User = get_user_model()

'''
    The authentication views are functional
'''

                                        # DATA FORMAT
'''
    Every data/information that will be sent to and recieved from this view (users) must be in JSON format.
    For example when signing up, the names,email,passwords and co should be sent in JSON format, not multipart, not 
    form data etc.
'''

@csrf_exempt
@api_view(['POST','PUT'])
def signup(request):
    try:
        
        data = JSONParser().parse(request)
        print(data)
        try:
            user = User.objects.create_user(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
                
            )
            if data['phone_number']:
                user.phone_number=data['phone_number']
            user.save()
        except:
            return JsonResponse({'error':'Data appears to be invalid or incomplete, check again'}, status=400)
        
        token = Token.objects.create(user=user)
        return JsonResponse({'token':str(token)}, status=201)
        return Response({'data':str(data)})
    except IntegrityError:
        return JsonResponse({'error':'Username or email taken, choose another'}, status=400)
{
"first_name": "Iyke",
"last_name": "Andy",
"email": "a@a.com",
"password": "andy10"
}
# class SignUp(APIView):
#     def post(self, request):
#         data = request.data
#         try:
#             user = User.objects.create_user(
#                 first_name=data['first_name'],
#                 last_name=data['last_name'],
#                 email=data['email'],
#                 password=data['password']
#             )
#             user.save()
#         except:
#             return JsonResponse({'error':'Data appears to be invalid or incomplete, check again'}, status=400)
        
#         token = Token.objects.create(user=user)
#         return JsonResponse({'token':str(token)}, status=201)
#         # return Response({'detail':'Shit', 'data':str(request.data)})

@csrf_exempt
@api_view(['POST'])
def login(request):  
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = authenticate(
                email=data['email'],
                password=data['password']
            )
        except:
            return JsonResponse({'error':'Data appears to be invalid or incomplete, check again'}, status=400)
        if user is None:
            return JsonResponse({'error':'unable to login, check email and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=200)
    return JsonResponse({'error':'something went wrong'}, status=400)

@permission_classes([permissions.IsAuthenticated])
@api_view(['GET', 'POST'])
def update_user(request):
    if request.method == 'GET':
        user = get_object_or_404(User, id=request.user.id)
        data = {
            'id':user.id,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,
            'phone_number':user.phone_number
        }
        return JsonResponse(data, status=200)

    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id)
        data = JSONParser().parse(request)
        try:
            if data['first_name']:
                user.first_name=data['first_name']
            if data['last_name']:
                user.last_name=data['last_name']
            if data['email']:
                user.email=data['email']
            if data['phone_number']:
                user.phone_number=data['phone_number']
            if data['password']:
                user.set_password=data['password']
            user.save()
        except:
            return JsonResponse({'error':'Data appears to be invalid or incomplete, check again'}, status=200)
        
        updated_data = {
            'id':user.id,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,
            'phone_number':user.phone_number
        }
        return JsonResponse(updated_data, status=200)

@permission_classes([permissions.IsAuthenticated])
@csrf_exempt
@api_view(['POST'])
def logout(request):
    try:
        token = Token.objects.get(id=request.user.id)
        token.delete()
        return JsonResponse({'detail':'user logged out successfully'}, status=200)
    except:
        return JsonResponse({'error':'user not found'}, status=400)