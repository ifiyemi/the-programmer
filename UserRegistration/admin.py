from django.contrib import admin
from  .models import RegDetails
# Register your models here.

class SomeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', '__str__']

admin.site.register(RegDetails, SomeModelAdmin)




