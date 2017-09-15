# -*- coding:utf-8 -*-  

'''
Created on 2017年9月1日

@author: Jim

'''
import json
import requests
import xlrd
# import xlwt
from xlutils.copy import copy
from PublicTools.GetTestDataPath import GetTestDataPath

Testdata = xlrd.open_workbook(GetTestDataPath())#打开测试数据，路径需要自己配，相对路径似乎不行
table = Testdata.sheets()[0]#选择sheet
hurl = table.cell(7,1).value#读取URL
def test_get_token():
    '''登陆'''
    husername = table.cell(3,1).value
    hpassword = table.cell(4,1).value
    hotp = table.cell(5,1).value
    hcontent_type = table.cell(6,1).value
    hdata = {
        "username":husername,
        "password":hpassword,
        "otp":hotp}
    headers = {'content-type': hcontent_type
       }
    r = requests.post(hurl+'/login', data=json.dumps(hdata), headers=headers)
    hjson = json.loads(r.text)#获取并处理返回的json数据
    herror ="error"
    if herror in hjson:   
        print("登陆失败，退出程序！")
        exit()
    else:
        hcode = str(hjson['status'])
        print('请求返回状态为：'+hcode)
        if hcode == table.cell(9,1).value:   
            token = hjson['data']['token']#获取token
            print('当前token为：'+token)    
            #将获取的TOKEN保存到testdata中 
            oldWb = xlrd.open_workbook(GetTestDataPath(),formatting_info=True)
            newWb = copy(oldWb)
            newWs = newWb.get_sheet(0)
            newWs.write(8, 1, token)
            print ("Token写入成功")
            newWb.save(GetTestDataPath())#路径需要自己配，相对路径似乎不行
            print ("TestdDate保存成功")
            
        else:
            print('登陆失败，程序退出')
            exit()
        

  
# test_get_token()    
    
