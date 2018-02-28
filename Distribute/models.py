from django.db import models
from django.utils import timezone
# Create your models here.


class NRecord(models.Model):
    '''
        record_no 叫号的卡号或证件号
        record_date 叫号的时间
        record_status 客户状态：0-等待服务，1-正在服务，2-服务结束

    status = models.IntegerField(default=0)
    no = models.CharField(max_length=22)
    arrive_datetime = models.DateTimeField('DateTime Record')  # 取号时间
    start_date = models.DateTimeField('Date Record',default=timezone.now)  # 叫号时间或开始服务时间
    end_date = models.DateTimeField('Date Record',default=timezone.now)  # 结束服务时间
    wait_no = models.CharField(max_length=10) #排队编号

    def __str__(self):
        return self.arrive_date.strftime("%Y-%m-%d %H:%M:%S") + "  卡号：" + self.no
    '''
    status = models.IntegerField(default=0)
    no = models.CharField(max_length=22)
    arrive_date = models.DateTimeField('Date Record')  # 取号时间
    start_date = models.DateTimeField('Date Record', default=timezone.now)  # 叫号时间或开始服务时间
    end_date = models.DateTimeField('Date Record', default=timezone.now)  # 结束服务时间
    wait_no = models.CharField(max_length=10)  # 排队编号

    def __str__(self):
        return  self.arrive_date.strftime("%Y-%m-%d %H:%M:%S") + "  卡号：" + self.no

class VRecord(models.Model):
    '''
        record_no 叫号的卡号或证件号
        record_date 叫号的时间
        record_cust_level 客户等级：0-普通客户，1-VIP客户，2-超级VIP
        record_status 客户状态：0-等待服务，1-正在服务，2-服务结束
    '''
    status = models.IntegerField(default=0)
    no = models.CharField(max_length=22)
    arrive_date = models.DateTimeField('Date Record')  # 取号时间
    start_date = models.DateTimeField('Date Record',default=timezone.now)  # 叫号时间或开始服务时间
    end_date = models.DateTimeField('Date Record',default=timezone.now)  # 结束服务时间
    wait_no = models.CharField(max_length=10) #排队编号

    def __str__(self):
        return  self.arrive_date.strftime("%Y-%m-%d %H:%M:%S") + "  卡号：" + self.no



