from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterUserSerializer
from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.reverse import reverse
import requests





class RegisterUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer
    
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = get_user_model().objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found!')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect Password!')
    
    response = Response()
    
    token_endpoint = reverse(viewname='token_obtain_pair', request=request)
    tokens = requests.post(token_endpoint, data=request.data).json()
    
    response.data = {
        'access_token': tokens.get('access'),
        'refresh_token': tokens.get('refresh'),
        'email': user.email
    }
    
    return response
    
    
