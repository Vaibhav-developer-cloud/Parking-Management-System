from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Building)
admin.site.register(Rows)
admin.site.register(Floor)
admin.site.register(Column)
admin.site.register(Vehical)
admin.site.register(Parking)



