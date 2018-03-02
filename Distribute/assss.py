from django.shortcuts import render
from . import oper
from .oper import OperateOrder
from django.http import HttpResponse



# Create your views here.

windows_id=''


def index(request):
    windows_id = 2
    OperateOrder.wait_cust=OperateOrder.get_new_record(windows_id)
    if OperateOrder.wait_cust:
        tips = '请' + OperateOrder.wait_cust[0].wait_no + '到' + str(OperateOrder.wait_cust[0].service_window) + '号窗口办理业务'
    else:
        tips = None

    #return render(request, 'Distribute/index.html', {'tips': tips})
    return HttpResponse(OperateOrder.wait_cust[0].wait_no)


def normal(request):
    OperateOrder.insert_new_record('00112',0)
    if OperateOrder.wait_cust:
        tips = '请' + OperateOrder.wait_cust[0].wait_no + '到' + str(OperateOrder.wait_cust[0].service_window) + '号窗口办理业务'
    else:
        tips = None

    #return render(request, 'Distribute/index.html', {'tips': tips})
    return HttpResponse(OperateOrder.wait_cust[0].wait_no)


def vip(request):
    OperateOrder.insert_new_record('00113', 1)
    if OperateOrder.wait_cust:
        tips = '请' + OperateOrder.wait_cust[0].wait_no + '到' + str(OperateOrder.wait_cust[0].service_window) + '号窗口办理业务'
    else:
        tips = None

    #return render(request, 'Distribute/index.html', {'tips': tips})
    return HttpResponse(OperateOrder.wait_cust[0].wait_no)


def next(request ):
    windows_id = 1
    OperateOrder.wait_cust=OperateOrder.get_new_record(windows_id)
    if OperateOrder.wait_cust:
        tips = '请' + OperateOrder.wait_cust[0].wait_no + '到' + str(OperateOrder.wait_cust[0].service_window) + '号窗口办理业务'
    else:
        tips = None

    #return render(request, 'Distribute/index.html', {'tips': tips})
    return HttpResponse(OperateOrder.wait_cust[0].wait_no)
