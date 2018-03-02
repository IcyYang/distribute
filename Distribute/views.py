from .oper import OperateOrder
from django.http import HttpResponse



# Create your views here.

windows_id=''


def index(request):
    waitno = OperateOrder.insert_new_record('00112', 0)
    return HttpResponse(waitno)


def normal(request):
    waitno = OperateOrder.insert_new_record('00112',0)
    return HttpResponse(waitno)


def vip(request):
    waitno = OperateOrder.insert_new_record('00112', 1)
    return HttpResponse(waitno)


def next(request ):
    windows_id = 1
    OperateOrder.wait_cust=OperateOrder.get_new_record(windows_id)
    if OperateOrder.wait_cust:
        tips = '请' + OperateOrder.wait_cust[0].wait_no + '到' + str(OperateOrder.wait_cust[0].service_window) + '号窗口办理业务'
    else:
        tips = None

    #return render(request, 'Distribute/index.html', {'tips': tips})
    return HttpResponse(tips)
