from django.contrib import admin
from .models import Clients, Cars, Orders, Users
# Register your models here.
admin.site.register(Clients)
admin.site.register(Cars)
admin.site.register(Orders)
admin.site.register(Users)

