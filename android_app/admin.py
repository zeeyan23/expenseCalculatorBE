from django.contrib import admin
from android_app.models import *
# Register your models here.

class AllRecordsAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','credited_date','createdDate','modifiedDate')
    list_display_links = ('id', 'name') 


admin.site.register(all_records,AllRecordsAdmin)
