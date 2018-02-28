from django.shortcuts import render
from django.http import HttpResponse
from Distribute.models import NRecord,VRecord
from django.utils import timezone
import datetime
from .generatenum import GenerateOrder

# Create your views here.
normal=0
vip=1

def index(request):
    return HttpResponse("Hello, world. You're at the Distribute index.")


def get_new_record():
    latest_record = VRecord.objects.filter(status__exact=0).order_by('id')[:1]
    if len(latest_record) ==0:
        latest_record = NRecord.objects.filter(status__exact=0).order_by('id')[:1]
        if len(latest_record) > 0:
            NRecord.objects.filter(wait_no__exact=latest_record[0].wait_no).update(status=1,start_date=timezone.now())
            return latest_record[0].wait_no
        else:
            return 'noRecord'
    else:
        VRecord.objects.filter(wait_no__exact=latest_record[0].wait_no).update(status=1,start_date=timezone.now())
        return latest_record[0].wait_no


def insert_new_record(custom_no,custom_level):
    date = timezone.now()
    if custom_level == normal:
        latest_record = NRecord.objects.filter(status__exact=0).order_by('-id')[:1]
        if (len(latest_record) > 0) & (latest_record[0].arrive_date >= timezone.now() - datetime.timedelta(days=1)):
                waitno = latest_record[0].wait_no
                GenerateOrder.normal_number = int(waitno[1:len(waitno)])

        waitno = GenerateOrder.getnormalorder(5,'A')
        new_record = NRecord(no=custom_no, wait_no=waitno, arrive_date=date)
        new_record.save()
    elif  custom_level == vip:
        latest_record = VRecord.objects.filter(status__exact=0).order_by('-id')[:1]
        if (len(latest_record) > 0) & (latest_record[0].arrive_date >= timezone.now() - datetime.timedelta(days=1)):
                waitno = latest_record[0].wait_no
                GenerateOrder.vip_number = int(waitno[1:len(waitno)])
        waitno = GenerateOrder.getviporder(5,'V')
        new_record = VRecord(no=custom_no, wait_no=waitno, arrive_date=date)
        new_record.save()


def set_record_passed(waitno,custom_level):
    if custom_level == normal:
        NRecord.objects.filter(wait_no__exact=waitno).update(status=2,end_date=timezone.now())
    elif  custom_level == vip:
        NRecord.objects.filter(wait_no__exact=waitno).update(status=2,end_date=timezone.now())
