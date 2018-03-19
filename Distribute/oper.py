from Distribute.models import NRecord,VRecord,vipCust
from django.utils import timezone
from .generatenum import GenerateOrder
import json
import datetime
# Create your views here.


class OperateOrder:

    wait_cust=None

    @classmethod
    def get_new_record(cls,para):
        python_para = json.loads(para)
        bankid = python_para['bid']
        windowno = python_para['wid']
        institudeid = python_para['iid']


        now_time = timezone.now()
        latest_vrecord = VRecord.objects.filter(status__exact=0,
                                                arrive_date__date__exact=timezone.now().date(),
                                                bank_no__exact=bankid, institution_no__exact=institudeid).order_by(
            'id')[:1]
        if len(latest_vrecord) ==0:
            latest_nrecord = NRecord.objects.filter(status__exact=0,
                                                    arrive_date__date__exact=timezone.now().date(),
                                                    bank_no__exact=bankid, institution_no__exact=institudeid).order_by(
                'id')[:1]
            if len(latest_nrecord) == 0:
                return latest_nrecord
            else:
                NRecord.objects.filter(wait_no__exact=latest_nrecord[0].wait_no,
                                       arrive_date__date__exact=timezone.now().date(), bank_no__exact=bankid,
                                       institution_no__exact=institudeid).update(
                    status=1,
                    start_date=timezone.now(),
                    service_window=windowno)
                latest_record = NRecord.objects.filter(wait_no__exact=latest_nrecord[0].wait_no,
                                                       arrive_date__date__exact=timezone.now().date(),
                                                       bank_no__exact=bankid, institution_no__exact=institudeid)
                return latest_record

        else:
            VRecord.objects.filter(wait_no__exact=latest_vrecord[0].wait_no,
                                   arrive_date__date__exact=timezone.now().date(), bank_no__exact=bankid,
                                   institution_no__exact=institudeid).update(
                status=1,
                start_date=timezone.now(),
                service_window=windowno)

            latest_record = VRecord.objects.filter(wait_no__exact=latest_vrecord[0].wait_no,
                                                   arrive_date__date__exact=timezone.now().date(),
                                                   bank_no__exact=bankid, institution_no__exact=institudeid)
            return latest_record

    @classmethod
    def insert_new_record(cls,para):
        python_para = json.loads(para)
        bankid = python_para['bid']
        terminalid = python_para['tid']
        custno = python_para['cid']
        institudeid = python_para['iid']

        isvip = vipCust.objects.filter(no__exact=custno)

        date = timezone.now()
        if len(isvip)==0:#普通号
            now_time = timezone.now()
            latest_record_today = NRecord.objects.filter(arrive_date__date__exact=timezone.now().date(),
                                                         bank_no__exact=bankid,
                                                         institution_no__exact=institudeid).order_by(
                '-id')[:1]

            if len(latest_record_today)>0:
                waitno = latest_record_today[0].wait_no
                GenerateOrder.normal_number = int(waitno[1:len(waitno)])
            else:
                GenerateOrder.normal_number = 0

            waitno = GenerateOrder.getnormalorder(5,'A')
            new_record = NRecord(no=custno, wait_no=waitno, terminal_no=terminalid,bank_no=bankid,institution_no=institudeid)
            new_record.save()
        else:
            now_time = timezone.now()
            latest_record_today = VRecord.objects.filter(arrive_date__date__exact=timezone.now().date(),
                                                         bank_no__exact=bankid,
                                                         institution_no__exact=institudeid).order_by(
                '-id')[:1]

            if len(latest_record_today) > 0:
                waitno = latest_record_today[0].wait_no
                GenerateOrder.vip_number = int(waitno[1:len(waitno)])
            else:
                GenerateOrder.vip_number = 0

            waitno = GenerateOrder.getviporder(5,'V')
            new_record = VRecord(no=custno, wait_no=waitno, terminal_no=terminalid,bank_no=bankid,isVIP=True,institution_no=institudeid)
            new_record.save()

        return new_record.wait_no

    @classmethod
    def set_record_passed(cls,para):
        python_para = json.loads(para)
        waitno = python_para['wait_no']
        spe_status = python_para['status']
        bankid = python_para['bid']
        institudeid = python_para['iid']

        spe_record_today = NRecord.objects.filter(arrive_date__date__exact=timezone.now().date(),
                                                     bank_no__exact=bankid,wait_no__exact=waitno,institution_no__exact=institudeid)

        if len(spe_record_today) ==0:
            spe_record_today = VRecord.objects.filter(arrive_date__date__exact=timezone.now().date(),
                                                      bank_no__exact=bankid, wait_no__exact=waitno,institution_no__exact=institudeid)
            if len(spe_record_today) == 0:
                pass
            else:
                VRecord.objects.filter(wait_no__exact=waitno, bank_no__exact=bankid,
                                       arrive_date__date__exact=timezone.now().date(),institution_no__exact=institudeid).update(
                    status=spe_status, end_date=timezone.now())
        else:
            NRecord.objects.filter(wait_no__exact=waitno, bank_no__exact=bankid,
                                   arrive_date__date__exact=timezone.now().date(),institution_no__exact=institudeid).update(
                status=spe_status,
                end_date=timezone.now())

ssss=1