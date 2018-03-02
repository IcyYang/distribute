from django.contrib import admin
from Distribute.models import NRecord,VRecord
# Register your models here.


class NRecordAdmin(admin.ModelAdmin):
    list_display = ('no','wait_no','status','arrive_date')
    list_filter = ['wait_no']
    search_fields = ['wait_no']


class VRecordAdmin(admin.ModelAdmin):
    list_display = ('no','wait_no','status','arrive_date')
    list_filter = ['wait_no']
    search_fields = ['wait_no']


admin.site.register(NRecord,NRecordAdmin)
admin.site.register(VRecord,VRecordAdmin)