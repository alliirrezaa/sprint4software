from django.shortcuts import render,redirect
from home.models import Forms
from ..models import Cart
from .serializers import CartSerializer
from rest_framework import status,mixins,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

@api_view(['POST',])
def add_cart(request,id):
    form=Forms.objects.get(id=id)
    if request.method == 'POST':
        serializer=CartSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            cart=serializer.save(user_id=request.user)
            return Response({"Added": ["add shod!"]}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def remove_cart(request,id):
    Cart.objects.filter(id=id).delete()
    return Response({"Removed": ["remove shod!"]}, status=status.HTTP_200_OK)

class CartDetail(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)