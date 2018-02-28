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
    now_time = timezone.now()
    latest_record = VRecord.objects.filter(status__exact=0,arrive_date__gte=timezone.now() - datetime.timedelta(
                hours=now_time.hour) - datetime.timedelta(minutes=now_time.minute) - datetime.timedelta(
                seconds=now_time.second)).order_by('id')[:1]
    if len(latest_record) ==0:
        latest_record = NRecord.objects.filter(status__exact=0,arrive_date__gte=timezone.now() - datetime.timedelta(
                hours=now_time.hour) - datetime.timedelta(minutes=now_time.minute) - datetime.timedelta(
                seconds=now_time.second)).order_by('id')[:1]
        if len(latest_record) > 0:
            NRecord.objects.filter(wait_no__exact=latest_record[0].wait_no,arrive_date__gte=timezone.now() - datetime.timedelta(
                hours=now_time.hour) - datetime.timedelta(minutes=now_time.minute) - datetime.timedelta(
                seconds=now_time.second)).update(status=1,start_date=timezone.now())
            return latest_record[0].wait_no
        else:
            return 'noRecord'
    else:
        VRecord.objects.filter(wait_no__exact=latest_record[0].wait_no).update(status=1,start_date=timezone.now())
        return latest_record[0].wait_no


def insert_new_record(custom_no,custom_level):
    date = timezone.now()
    if custom_level == normal:
        #latest_record_today = NRecord.objects.filter(arrive_date__gte=timezone.now() - datetime.timedelta(days=1)).order_by('-id')[:1]#今天的最新号码
        now_time = timezone.now()
        latest_record_today = NRecord.objects.filter(
            arrive_date__gte=timezone.now() - datetime.timedelta(
                hours=now_time.hour) - datetime.timedelta(minutes=now_time.minute) - datetime.timedelta(
                seconds=now_time.second)).order_by('-id')[:1]

        if len(latest_record_today)>0:
            waitno = latest_record_today[0].wait_no
            GenerateOrder.normal_number = int(waitno[1:len(waitno)])
        else:
            GenerateOrder.normal_number = 0

        waitno = GenerateOrder.getnormalorder(5,'A')
        new_record = NRecord(no=custom_no, wait_no=waitno, arrive_date=date)
        new_record.save()
    elif  custom_level == vip:
        now_time = timezone.now()
        latest_record_today = VRecord.objects.filter(
            arrive_date__gte=timezone.now() - datetime.timedelta(
                hours=now_time.hour) - datetime.timedelta(minutes=now_time.minute) - datetime.timedelta(
                seconds=now_time.second)).order_by('-id')[:1]

        if len(latest_record_today) > 0:
            waitno = latest_record_today[0].wait_no
            GenerateOrder.vip_number = int(waitno[1:len(waitno)])
        else:
            GenerateOrder.vip_number = 0

        waitno = GenerateOrder.getviporder(5,'V')
        new_record = VRecord(no=custom_no, wait_no=waitno, arrive_date=date)
        new_record.save()


def set_record_passed(waitno,custom_level):
    now_time = timezone.now()
    if custom_level == normal:#将今天的某个排队号码状态设置为已过号
        NRecord.objects.filter(wait_no__exact=waitno,arrive_date__gte=timezone.now() -  datetime.timedelta(
                hours=now_time.hour) - datetime.timedelta(minutes=now_time.minute) - datetime.timedelta(
                seconds=now_time.second)).update(status=2,end_date=timezone.now())
    elif  custom_level == vip:
        VRecord.objects.filter(wait_no__exact=waitno,arrive_date__gte=timezone.now() - datetime.timedelta(
                hours=now_time.hour) - datetime.timedelta(minutes=now_time.minute) - datetime.timedelta(
                seconds=now_time.second)).update(status=2,end_date=timezone.now())
