from django.urls import path,include
from .views import *
from rest_framework import routers

app_name='home'

router=routers.SimpleRouter()
router.register('faq',faqList)
router.register('category',CategoryList)
router.register('product',ProductList)
router.register('forms',FormsList)
"""router.register('offsetform',OffsetFormList)
router.register('subform',SublimitionFormList)"""

urlpatterns = [
    path('',include(router.urls)),
    path('contact/',contact,name='contact'),
    path('form/<int:id>/',forms,name='forms'),
]
