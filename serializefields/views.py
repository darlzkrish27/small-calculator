from rest_framework.response import Response 
from .serializers import SumSerializer
from rest_framework import status,views,generics
from django.shortcuts import render

class SumView(generics.CreateAPIView):
    serializer_class = SumSerializer
    def post(self, request, format=None):
        serializer = SumSerializer(data=request.data)
        if serializer.is_valid():
            a = serializer.validated_data.get('num1')
            
            b = serializer.validated_data.get('num2')
            s = serializer.data
            if(serializer.validated_data.get('option')=='+'):
            	s.update({'sum': a+b})

            elif(serializer.validated_data.get('option')=='-'):
            	s.update({'diff': a-b})
            
            elif(serializer.validated_data.get('option')=='*'):
            	s.update({'mul': a*b})
            
            elif(serializer.validated_data.get('option')=='%'):
            	s.update({'div': a/b})
            return Response(s,status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 