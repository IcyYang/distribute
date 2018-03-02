from django.db import models
from django.utils import timezone
# Create your models here.


class NRecord(models.Model):
    '''
        record_no 叫号的卡号或证件号
        record_date 叫号的时间
        record_status 客户状态：0-等待服务，1-正在服务，2-服务结束
        service_window服务窗口
    '''
    status = models.IntegerField(default=0)
    service_window = models.IntegerField(default=0)
    no = models.CharField(max_length=22)
    arrive_date = models.DateTimeField('GetNo DateTime')  # 取号时间
    start_date = models.DateTimeField('Start Service DateTime', default=timezone.now)  # 叫号时间或开始服务时间
    end_date = models.DateTimeField('End Service DateTime', default=timezone.now)  # 结束服务时间
    wait_no = models.CharField(max_length=10)  # 排队编号

    def __str__(self):
        return  self.arrive_date.strftime("%Y-%m-%d %H:%M:%S") + "  卡号：" + self.no

class VRecord(models.Model):
    '''
        record_no 叫号的卡号或证件号
        record_date 叫号的时间
        record_status 客户状态：0-等待服务，1-正在服务，2-服务结束
        service_window服务窗口
    '''
    status = models.IntegerField(default=0)
    service_window = models.IntegerField(default=0)
    no = models.CharField(max_length=22)
    arrive_date = models.DateTimeField('Date Record')  # 取号时间
    start_date = models.DateTimeField('Date Record',default=timezone.now)  # 叫号时间或开始服务时间
    end_date = models.DateTimeField('Date Record',default=timezone.now)  # 结束服务时间
    wait_no = models.CharField(max_length=10) #排队编号

    def __str__(self):
        return  self.arrive_date.strftime("%Y-%m-%d %H:%M:%S") + "  卡号：" + self.no



