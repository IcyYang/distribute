from .oper import OperateOrder
from django.http import HttpResponse
from django.shortcuts import render
import json


# Create your views here.
#取号
def getorder(request):

    '''
    para = request.GET['para']
    python_para = json.loads(para)
    bankid = python_para['bid']
    terminalid = python_para['tid']
    custno = python_para['cid']
    '''
    institudeid = request.GET['iid']#机构号
    bankid = request.GET['bid']#分行号
    terminalid = request.GET['tid']#终端号
    custno = request.GET['cid']
    data = {'iid':institudeid,'bid':bankid, 'tid':terminalid, 'cid':custno}
    python_para = json.dumps(data)

    waitno = OperateOrder.insert_new_record(python_para)
    return HttpResponse(waitno)

"""
def index(request):
    waitno = OperateOrder.insert_new_record('00112', 0)
    return HttpResponse(waitno)
    
    
def vip(request):
    waitno = OperateOrder.insert_new_record('00112', 1)
    return HttpResponse(waitno)
"""


#叫号
def next(request):
    institudeid = request.GET['iid']  # 机构号
    bankid = request.GET['bid']
    windows_id  = request.GET['wid']
    data = {'iid':institudeid,'bid': bankid, 'wid': windows_id}
    python_para = json.dumps(data)
    OperateOrder.wait_cust=OperateOrder.get_new_record(python_para)
    if OperateOrder.wait_cust:
        tips = '请' + OperateOrder.wait_cust[0].wait_no + '到' + str(OperateOrder.wait_cust[0].service_window) + '号窗口办理业务'
    else:
        tips = None

    #return render(request, 'Distribute/index.html', {'tips': tips})
    return HttpResponse(tips)
