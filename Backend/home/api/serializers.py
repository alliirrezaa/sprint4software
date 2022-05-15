from rest_framework import serializers
from ..models import *

class ContactSerializer(serializers.Serializer):
    subject=serializers.CharField(max_length=20)
    email=serializers.EmailField(max_length=20)
    message=serializers.CharField(max_length=20)
    
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model=faq
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Forms
        fields='__all__'

    def update(self, instance, validated_data):
        request = self.context.get("request")
        #get new data
        new_store_name=validated_data['store_name']
        new_job=validated_data['job']
        new_management = validated_data['management']
        new_media_address = validated_data['media_address']
        new_mobile=validated_data['mobile']
        new_landline=validated_data['landline']
        new_quantity= validated_data['quantity']
        new_material= validated_data['material']
        new_information= validated_data['information']
        new_length= validated_data['length']
        new_width= validated_data['width']
        #update Profile data
        instance.store_name =new_store_name
        instance.job = new_job
        instance.management=new_management
        instance.media_address=new_media_address
        instance.mobile=new_mobile
        instance.landline=new_landline
        instance.quantity=new_quantity
        instance.material=new_material
        instance.information=new_information
        instance.length=new_length
        instance.width=new_width
        instance.save()
        return instance
        """request = self.context.get("request")
        print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
        form=Forms(
            product=Product.objects.get(id=request.id),
            store_name=self.validated_data['store_name'],
            job=self.validated_data['job'],
            management=self.validated_data['management'],
            media_address=self.validated_data['media_address'],
            mobile=self.validated_data['mobile'],
            landline=self.validated_data['landline'],
            quantity=self.validated_data['quantity'],
            material=self.validated_data['material'],
            information=self.validated_data['information'],
            length=self.validated_data['length'],
            width=self.validated_data['width'],
        )
        form.save()
        return form"""

"""class OffsetFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=OffsetForm
        fields='__all__'
        extra_kwargs={
            'category':{'read_only':True},
        }
    
    def save(self):
        ofform=OffsetForm(
            category=Category.objects.get(name='Offset'),
            store_name=self.validated_data['store_name'],job=self.validated_data['job'],
            management=self.validated_data['management'],media_address=self.validated_data['media_address'],
            mobile=self.validated_data['mobile'],landline=self.validated_data['landline']
        )
        ofform.save()
        return ofform

class SublimitionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=SublimitionForm
        fields='__all__'
        extra_kwargs={
            'category':{'read_only':True},
        }
    
    def save(self):
        subform=SublimitionForm(
            category=Category.objects.get(name='Sublimition'),
            quantity=self.validated_data['quantity'],material=self.validated_data['material'],
            information=self.validated_data['information'],image=self.validated_data['image'],
            length=self.validated_data['length'],width=self.validated_data['width']
        )
        subform.save()
        return subform"""


















"""class OffsetFormserializer(serializers.ModelSerializer):
    class Meta:
        model=offsetForm
        fields='__all__'
    
    def save(self):
        offsetform=offsetForm(
            store_name=self.validated_data['store_name'],
            job=self.validated_data['job'],management=self.validated_data['management'],
            media_address=self.validated_data['media_address'],mobile=self.validated_data['mobile'],
            landline=self.validated_data['landline']
        )
        offsetform.save()
        return offsetform
    
class SublimitionFormserializer(serializers.ModelSerializer):
    class Meta:
        model=sublimitionForm
        fields='__all__'
        
    def save(self):
        subform=sublimitionForm(
            quantity=self.validated_data['quantity'],
            material=self.validated_data['material'],information=self.validated_data['information'],
            length=self.validated_data['length'],width=self.validated_data['width']
        )
        subform.save()
        return subform"""