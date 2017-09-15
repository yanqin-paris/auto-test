# -*- coding:utf-8 -*-

'''
Created on 2017年9月2日

@author: Jim
'''
import json
import requests

hlist = []  # 添加一个数组，用来装测试结果


def TestPostRequest(hurl, hdata, headers, htestcassid, htestcassname, htesthope, fanhuitesthope):
    hr = requests.post(hurl, data=json.dumps(hdata), headers=headers)
    hjson = json.loads(hr.text)  # 获取并处理返回的json数据
    herror = "error"
    if herror in hjson:
        hstatus = str(hjson["status"])
        if hstatus == htesthope and fanhuitesthope in str(hjson):
            hhhdata = {"t_id": htestcassid,
                       "t_name": htestcassname,
                       "t_method": "post",
                       "t_url": hurl,
                       "t_param": "测试数据:" + str(hdata),
                       "t_hope": "status:" + str(htesthope),
                       "t_actual": "status:" + hstatus + ";msg:" + str(hjson),
                       "t_result": "通过"}
            hlist.append(hhhdata)  # 把测试结果添加到数组里面
            print(htestcassname)
            print("测试通过")
            print("返回的消息是：" + str(hjson))
        else:
            hhhdata = {"t_id": htestcassid,
                       "t_name": htestcassname,
                       "t_method": "post",
                       "t_url": hurl,
                       "t_param": "测试数据:" + str(hdata),
                       "t_hope": "status:" + str(htesthope),
                       "t_actual": str(hjson),
                       "t_result": "失败"}
            hlist.append(hhhdata)
            print(htestcassname)
            print('测试不通过')
            print("返回的消息为：" + str(hjson))
    else:
        hcode = str(hjson['status'])
        if hcode == htesthope and fanhuitesthope in str(hjson):
            hhhdata = {"t_id": htestcassid,
                       "t_name": htestcassname,
                       "t_method": "post",
                       "t_url": hurl,
                       "t_param": "测试数据:" + str(hdata),
                       "t_hope": "status:" + str(htesthope),
                       "t_actual": "status:" + hcode + ";msg:" + str(hjson),
                       "t_result": "通过"}
            hlist.append(hhhdata)  # 把测试结果添加到数组里面
            print(htestcassname)
            print("测试通过")
            print("返回的消息是：" + str(hjson))
        else:
            hhhdata = {"t_id": htestcassid,
                       "t_name": htestcassname,
                       "t_method": "post",
                       "t_url": hurl,
                       "t_param": "测试数据:" + str(hdata),
                       "t_hope": "status:" + str(htesthope),
                       "t_actual": "status:" + hcode + ";msg:" + str(hjson),
                       "t_result": "失败"}
            hlist.append(hhhdata)
            print(htestcassname)
            print('测试不通过')
            print("返回的消息是：" + str(hjson))


def TestGetRequest(hurl, hdata, headers, htestcassid, htestcassname, htesthope, fanhuitesthope):

    hr = requests.get(hurl, params=hdata, headers=headers)
    hjson = json.loads(hr.text)  # 获取并处理返回的json数据

    herror = "error"
    if herror in hjson:
        hstatus = str(hjson["status"])
        if hstatus == htesthope and fanhuitesthope in str(hjson):
            hhhdata = {"t_id": htestcassid,
                       "t_name": htestcassname,
                       "t_method": "get",
                       "t_url": hurl,
                       "t_param": "测试数据:" + str(hdata),
                       "t_hope": "status:" + str(htesthope),
                       "t_actual": "status:" + hstatus + ";msg:" + str(hjson),
                       "t_result": "通过"}
            hlist.append(hhhdata)  # 把测试结果添加到数组里面
            print(htestcassname)
            print("测试通过")
            print("返回的消息是：" + str(hjson))
        else:
            hhhdata = {"t_id": htestcassid,
                       "t_name": htestcassname,
                       "t_method": "get",
                       "t_url": hurl,
                       "t_param": "测试数据:" + str(hdata),
                       "t_hope": "status:" + str(htesthope),
                       "t_actual": str(hjson),
                       "t_result": "失败"}
            hlist.append(hhhdata)
            print(htestcassname)
            print('测试不通过')
            print("返回的消息为：" + str(hjson))
    else:
        hcode = str(hjson['status'])
        if hcode == htesthope and fanhuitesthope in str(hjson):
            hhhdata = {"t_id": htestcassid,
                       "t_name": htestcassname,
                       "t_method": "get",
                       "t_url": hurl,
                       "t_param": "测试数据:" + str(hdata),
                       "t_hope": "status:" + str(htesthope),
                       "t_actual": "status:" + hcode + ";data:" + str(hjson),
                       "t_result": "通过"}
            hlist.append(hhhdata)  # 把测试结果添加到数组里面
            print(htestcassname)
            print("测试通过")
            print("返回的消息是：" + str(hjson))
        else:
            hhhdata = {"t_id": htestcassid,
                       "t_name": htestcassname,
                       "t_method": "get",
                       "t_url": hurl,
                       "t_param": "测试数据:" + str(hdata),
                       "t_hope": "status:" + str(htesthope),
                       "t_actual": "status:" + hcode + ";msg:" + str(hjson),
                       "t_result": "失败"}
            hlist.append(hhhdata)
            print(htestcassname)
            print('测试不通过')
            print("返回的消息是：" + str(hjson))
