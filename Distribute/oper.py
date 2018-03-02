from Distribute.models import NRecord,VRecord
from django.utils import timezone
from .generatenum import GenerateOrder

# Create your views here.


class OperateOrder:
    normal=0
    vip=1
    wait_cust=None

    @classmethod
    def get_new_record(cls,win_no):
        now_time = timezone.now()
        latest_vrecord = VRecord.objects.filter(status__exact=0,
                                                arrive_date__date__exact=timezone.now().date()).order_by('id')[:1]
        if len(latest_vrecord) ==0:
            latest_nrecord = NRecord.objects.filter(status__exact=0,
                                                    arrive_date__date__exact=timezone.now().date()).order_by('id')[:1]
            if len(latest_nrecord) == 0:
                return latest_nrecord
            else:
                NRecord.objects.filter(wait_no__exact=latest_nrecord[0].wait_no,
                                       arrive_date__date__exact=timezone.now().date()).update(status=1,
                                                                                              start_date=timezone.now(),
                                                                                              service_window=win_no)

                latest_record = NRecord.objects.filter(wait_no__exact=latest_nrecord[0].wait_no,
                                                       arrive_date__date__exact=timezone.now().date())
                return latest_record

        else:
            VRecord.objects.filter(wait_no__exact=latest_vrecord[0].wait_no,
                                   arrive_date__date__exact=timezone.now().date()).update(status=1,
                                                                                          start_date=timezone.now(),
                                                                                          service_window=win_no)

            latest_record = VRecord.objects.filter(wait_no__exact=latest_vrecord[0].wait_no,
                                                   arrive_date__date__exact=timezone.now().date())
            return latest_record

    @classmethod
    def insert_new_record(cls,custom_no,custom_level):
        date = timezone.now()
        if custom_level == cls.normal:
            now_time = timezone.now()
            latest_record_today = NRecord.objects.filter(arrive_date__date__exact=timezone.now().date()).order_by(
                '-id')[:1]

            if len(latest_record_today)>0:
                waitno = latest_record_today[0].wait_no
                GenerateOrder.normal_number = int(waitno[1:len(waitno)])
            else:
                GenerateOrder.normal_number = 0

            waitno = GenerateOrder.getnormalorder(5,'A')
            new_record = NRecord(no=custom_no, wait_no=waitno, arrive_date=date)
            new_record.save()
        elif  custom_level == cls.vip:
            now_time = timezone.now()
            latest_record_today = VRecord.objects.filter(arrive_date__date__exact=timezone.now().date()).order_by(
                '-id')[:1]

            if len(latest_record_today) > 0:
                waitno = latest_record_today[0].wait_no
                GenerateOrder.vip_number = int(waitno[1:len(waitno)])
            else:
                GenerateOrder.vip_number = 0

            waitno = GenerateOrder.getviporder(5,'V')
            new_record = VRecord(no=custom_no, wait_no=waitno, arrive_date=date)
            new_record.save()

        return new_record.wait_no

    @classmethod
    def set_record_passed(cls,waitno,custom_level):
        now_time = timezone.now()
        if custom_level == cls.normal:
            # 将当天的某个排队号码状态设置为已过号
            NRecord.objects.filter(wait_no__exact=waitno, arrive_date__date__exact=timezone.now().date()).update(status=2,
                                                                                                               end_date=timezone.now())
        elif  custom_level == cls.vip:
            VRecord.objects.filter(wait_no__exact=waitno,arrive_date__date__exact=timezone.now().date()).update(status=2,end_date=timezone.now())
