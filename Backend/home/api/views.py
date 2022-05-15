from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from .serializers import *
from rest_framework import status,mixins,generics
from rest_framework.views import APIView
from ..models import *
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView

@api_view(['POST',])
def contact(request):
    serializer=ContactSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        data['subject']=request.data['subject']
        data['email']=request.data['email']
        data['message']=request.data['message']
        body= data['subject']+' \n'+data['email']+' \n'+data['message']
        form=EmailMessage('contact us',body,'test',('software.proj.test@gmail.com',))
        form.send(fail_silently=False)
        return Response(data)
    else:
        return Response(serializer.errors)

class faqList(ModelViewSet):
    queryset=faq.objects.all()
    serializer_class=FAQSerializer

class CategoryList(ReadOnlyModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductList(ReadOnlyModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

"""class OffsetFormList(ModelViewSet):
    queryset=OffsetForm.objects.all()
    serializer_class=OffsetFormSerializer

class SublimitionFormList(ModelViewSet):
    queryset=sub.objects.all()
    serializer_class=SublimitionFormSerializer"""

class FormsList(ModelViewSet):
    queryset=Forms.objects.all()
    serializer_class=FormsSerializer


@api_view(['POST',])
def forms(request,id):
    prod=get_object_or_404(Product,id=id)
    data={}
    print('-----------------------------------------------')
    print(prod.name)
    print('-----------------------------------------------')
    if prod.name=='Visit Card':
        print('pppppppppppppppppppppppppppppppppppppppppppp')
        serializer=FormsSerializer(data=request.data)
        if serializer.is_valid():
            form=serializer.save(product=prod)
            data['store_name']=request.data['store_name']
            data['job']=request.data['job']
            data['mobile']=request.data['mobile']
            data['management']=request.data['management']
            data['media_address']=request.data['media_address']
            return Response(data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif prod.name=='Puzzle':
        serializer=FormsSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            form=serializer.save(product=prod)
            data['quantity']=request.data['quantity']
            data['material']=request.data['material']
            data['information']=request.data['information']    
            return Response(data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif prod.name=='Factor':
        serializer=FormsSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            form=serializer.save(product=prod)
            data['management']=request.data['management']
            data['media_address']=request.data['media_address']
            data['material']=request.data['material']
            data['information']=request.data['information']    
            return Response(data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'final':'nope'})

"""@api_view(['POST',])
def offsetform(request):
    if request.method == 'POST':
        serializer=OffsetFormSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            data['response']='Successful.'
            return Response(data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def subform(request):
    pass"""