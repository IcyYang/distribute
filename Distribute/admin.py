from django.contrib import admin
from Distribute.models import NRecord,VRecord,vipCust,Terminal,Bank,Institute
# Register your models here.
"""
admin.site.register(Terminal)
admin.site.register(Bank)
admin.site.register(Institute)
"""



class NRecordAdmin(admin.ModelAdmin):
    list_display = ('no','wait_no','status','arrive_date')
    list_filter = ['wait_no']
    search_fields = ['wait_no']


class vipCustAdmin(admin.ModelAdmin):
    list_display = ('no','openbankno')
    list_filter = ['no']


class VRecordAdmin(admin.ModelAdmin):
    list_display = ('no','wait_no','status','arrive_date')
    list_filter = ['wait_no']
    search_fields = ['wait_no']


class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_no','institute_no','address')
    list_filter = ['bank_no']


class TerminalAdmin(admin.ModelAdmin):
    list_display = ('terminal_no','bank_no','institute_no','address')
    list_filter = ['terminal_no']


class InstituteAdmin(admin.ModelAdmin):
    list_display = ('institute_no',)
    list_filter = ['institute_no']


admin.site.register(NRecord,NRecordAdmin)
admin.site.register(VRecord,VRecordAdmin)
admin.site.register(vipCust,vipCustAdmin)
admin.site.register(Terminal,TerminalAdmin)
admin.site.register(Bank,BankAdmin)
admin.site.register(Institute,InstituteAdmin)

