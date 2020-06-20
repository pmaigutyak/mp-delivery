
from modeltranslation.translator import translator

from delivery.models import Warehouse, Region, City, DeliveryMethod


translator.register(Region, fields=['name'])
translator.register(City, fields=['name'])
translator.register(Warehouse, fields=['name'])
translator.register(DeliveryMethod, fields=['name'])
