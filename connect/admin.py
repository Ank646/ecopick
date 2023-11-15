from django.contrib import admin
from .models import dcenter
from .models import userpro
from .models import order
admin.site.register(userpro)
# admin.site.register(picker)
admin.site.register(dcenter)
admin.site.register(order)
# Register your models here.
