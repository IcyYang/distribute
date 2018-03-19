from django.db import models
from django.utils import timezone
# Create your models here.


class NRecord(models.Model):
    """
        no 叫号的卡号或证件号
        arrive_date 叫号的时间
        status 客户状态：0-等待服务，1-正在服务，2-服务结束,3-客户不在（过号了需重新取号）
        window服务窗口
    """
    status = models.IntegerField(default=0)
    service_window = models.IntegerField(default=0)
    no = models.CharField(max_length=22)
    wait_no = models.CharField(max_length=10)  # 排队编号
    terminal_no = models.CharField(max_length=10)#设备号
    bank_no = models.CharField(max_length=10, blank=True, null=True)  # 机构号
    institution_no = models.CharField(max_length=10)#机构号
    arrive_date = models.DateTimeField('GetNo DateTime', default=timezone.now)  # 取号时间
    start_date = models.DateTimeField('Start Service DateTime', default=timezone.now)  # 叫号时间或开始服务时间
    end_date = models.DateTimeField('End Service DateTime', default=timezone.now)  # 结束服务时间
    isVIP = models.BooleanField(default=False)#是否VIP号

    def __str__(self):
        return self.arrive_date.strftime("%Y-%m-%d %H:%M:%S") + "  卡号：" + self.no


class vipCust(models.Model):
    no = models.CharField(max_length=22)
    openbankno = models.CharField('Open bank NO',max_length=10)
    def __str__(self):
        return self.no+ "|" + self.openbankno


class VRecord(models.Model):
    """
        no 叫号的卡号或证件号
        arrive_date 叫号的时间
        status 客户状态：0-等待服务，1-正在服务，2-服务结束,3-客户不在（过号了需重新取号）
        window服务窗口
    """
    status = models.IntegerField(default=0)
    service_window = models.IntegerField(default=0)
    no = models.CharField(max_length=22)
    wait_no = models.CharField(max_length=10)  # 排队编号
    terminal_no = models.CharField(max_length=10)  # 设备号
    bank_no = models.CharField(max_length=10)  # 分行号
    #institution_no = models.CharField(max_length=10,blank=True, null=True)  # 机构号
    institution_no = models.CharField(max_length=10, blank=True, null=True)  # 机构号
    arrive_date = models.DateTimeField('GetNo DateTime', default=timezone.now)  # 取号时间
    start_date = models.DateTimeField('Start Service DateTime', default=timezone.now)  # 叫号时间或开始服务时间
    end_date = models.DateTimeField('End Service DateTime', default=timezone.now)  # 结束服务时间
    isVIP = models.BooleanField(default=False)  # 是否VIP号

    def __str__(self):
        return self.arrive_date.strftime("%Y-%m-%d %H:%M:%S") + "  卡号：" + self.no


#机构表
class Institute(models.Model):
    institute_no = models.CharField(max_length=10)

    def __str__(self):
        return self.institute_no


#分行列表
class Bank(models.Model):
    institute_no = models.ForeignKey(Institute, on_delete=models.CASCADE)
    bank_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.bank_no


# 终端表
class Terminal(models.Model):
    institute_no = models.ForeignKey(Institute, on_delete=models.CASCADE)
    bank_no = models.ForeignKey(Bank, on_delete=models.CASCADE)
    terminal_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.terminal_no
