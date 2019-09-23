from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models.functions import Greatest
import pandas as pd
# Create your views here.

from .models import BankInfo

device_name = ['DIS7864654','DIS231434','DIS619613','DIS696737','DIS645389']

device_info = {
    'DIS7864654': '스마트폰',
    'DIS231434': '데스크탑 컴퓨터',
    'DIS619613': '노트북 컴퓨터',
    'DIS696737': '기타',
    'DIS645389': '스마트패드',
}

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def read(request):
#    with open('report.csv', newline='') as csvfile:
#        reader = csv.DictReader(csvfile)
    df = pd.read_csv('report.csv', sep=',')
    bulk_bankinfo = []
    for row in df.itertuples():
        year = row[1]
        use_rate = float(row[2])
        phone_rate = float(row[3])
        pc_rate = float(row[4])
        notebook_rate = float(row[5])
        etc_rate = float(row[6])
        print(etc_rate)
        if row[7] != '-':
            pad_rate = float(row[7])
        else:
            pad_rate = 0
        print(pad_rate)
        try:
            bulk_bankinfo.append(BankInfo(
                year=year,
                use_rate=use_rate,
                phone_rate=phone_rate,
                pc_rate=pc_rate,
                notebook_rate=notebook_rate,
                etc_rate=etc_rate,
                pad_rate=pad_rate
            ))
        except:
            return Response({"result": False, "error": "Something went wrong."})
    BankInfo.objects.bulk_create(bulk_bankinfo)
    return Response({"result": True, "response": "Read data from report.csv"})

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def deviceinfo(request):
    devices = []
    for key in device_info:
        devices += [{
            'device_id' : key,
            'device_name' : device_info[key]
        }]
    result = {'devices': devices}
    return JsonResponse(result)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def mostallyear(request):
    bankinfos = BankInfo.objects.all()
    devices = []
    for yearInfo in bankinfos:
        rate = [yearInfo.phone_rate, yearInfo.pc_rate, yearInfo.notebook_rate, yearInfo.etc_rate, yearInfo.pad_rate]
        device_index = rate.index(max(rate))
        devices += [{
            'year' : yearInfo.year,
            'device_id' : device_name[device_index],
            'device_name' : device_info[device_name[device_index]],
            'rate' : max(rate)
        }]
    result = {'devices': devices}
    return JsonResponse(result)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def mostinyear(request):
    s_year =  request.data['year']
    try:
        bankinfo = BankInfo.objects.get(year=s_year)
    except:
        return Response({"status": False, "error": "data does not exist."})
    rate = [bankinfo.phone_rate, bankinfo.pc_rate, bankinfo.notebook_rate, bankinfo.etc_rate, bankinfo.pad_rate]
    device_index = rate.index(max(rate))
    result = [{
        'year': bankinfo.year,
        'device_name': device_info[device_name[device_index]],
        'rate': max(rate)
    }]
    results = {'result':result}
    return JsonResponse(results)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def mostindevice(request):
    device_id = request.data['device_id']
    device_index = device_name.index(device_id)
    bankinfos = BankInfo.objects.all()
    max_rate = 0
    max_year = 0
    print(device_index)
    for bankinfo in bankinfos:
        rate = [bankinfo.phone_rate, bankinfo.pc_rate, bankinfo.notebook_rate, bankinfo.etc_rate, bankinfo.pad_rate]
        print(rate)
        for i, device_rate in enumerate(rate):
            if i == device_index:
                if device_rate > max_rate:
                    max_rate = device_rate
                    max_year = bankinfo.year
                    print(max_year)
    result = [{
        'device_name': device_info[device_id],
        'year': max_year,
        'rate': max_rate
    }]
    results = {'result': result}
    return JsonResponse(results)




#@api_view(['Get, POST'])
#@permission_classes((IsAuthenticated,))
#@authentication_classes((JSONWebTokenAuthentication,))
#def predictdevice(request):

