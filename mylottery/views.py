from django.shortcuts import render,HttpResponse

import common.common as com
import common.models as models

from firebase import firebase
from mylottery.models import users


import json

def user_reg(request):    
    innerScript = ""
    if request.POST:
        result = users(name = request.POST['name'],
                       passward = request.POST['passward'],
                       sex = request.POST['sex'],
                       birthday = request.POST['birthday'])              
        result.save()
        
        list = users.objects.filter(name=request.POST['name']) 
        if list != None:
            innerScript="<script>alert('"+ list[0].name  +" inserted')</script>"
        else:
            innerScript="<script>alert('insert fail')</script>"
    
    return render(request, "user_reg.html",{'innerScript':innerScript})

def CkeckKey(no,datas):
    key_id=""
    if datas != None:
        for key in datas:
            if no == datas[key]["no"]:
                key_id = key
                break
    return key_id

def firebase_operate(request):
    url="https://lottery-web-d3348.firebaseio.com"
    fb = firebase.FirebaseApplication(url,None)

# 新增
# =============================================================================
#     students=[
#             {'no':1,'name':'李天龍'},
#             {'no':2,'name':'方大同'},
#             {'no':3,'name':'周杰倫'}]
#     
#     for sutdent in students:
#         fb.post('/students',sutdent)
# =============================================================================

# 刪除    
# =============================================================================
#     datas =  fb.get('/students',None)
#     no = 1
#     key_id = CkeckKey(no,datas)
#     fb.delete('/students/' + key_id,None)
#     result = fb.get('/students',None)
# =============================================================================
    
# 修改
# =============================================================================
#     datas =  fb.get('/students',None)
#     no = 2
#     key_id = CkeckKey(no,datas)
#     data = {"no":int(2),"name":"梁靜茹"}
#     fb.put(url+'/students/',data=data,name=key_id)
# =============================================================================
    
    result =  fb.get('/students',None)
    return render(request, "firebase.html", {'result':result})     

def mylottery(request):
    mylottery = models.MyLottery.objects.all().order_by('-volume')
    innerHtml = com.get_table_tag(mylottery)
    return render(request, "myLottery.html", {'innerHtml':innerHtml}) 
    
def mylottery_add(request):
    return render(request, "myLottery-add.html")  
    
def mylottery_adding(request):
    if request.POST:
        sql = ""
        sql = "insert into My_Lottery(category,volume,date,no1,no2,no3,no4,no5,no6,no7,no8,no9,no10,no11,no12) "
        sql += "select"
        sql +="\"two_win\","
        
        if(request.POST['volume'] != ""):
            #期號
            sql +="\"" + str(request.POST['volume']) +"\"," 
        
        if(request.POST['date'] != ""):
            #開獎日期
            sql +="\"" + str(request.POST['date']) +"\","    
        
        if(request.POST['number'] != ""):
            numbers = []
            numbers = str(request.POST['number']).split(',')
            for i in range(0,len(numbers)):
                sql += numbers[i]   
                if(i==len(numbers)-1):
                    sql += " "
                else:
                    sql +=","          
        com.ExeSql(sql)
        
    mylottery = models.MyLottery.objects.all().order_by('-volume')
    innerHtml = com.get_table_tag(mylottery)
    return render(request, "myLottery.html", {'innerHtml':innerHtml})    

def ajax_post(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:   
        if(request.method == "GET"):
            return render(request, "ajax_post.html") 
        elif(request.method == "POST"):
            volume = request.POST.get('volume')
            date = request.POST.get('date')
            number = request.POST.get('number')

            if( volume != "" and date !="" and number !=""):
                pass
            else:
                ret['status'] = False
                ret['error'] = "攔位不得為空！"   
        
        
    except Exception as e:
        ret['status'] = False
        ret['error'] = '請求錯誤'
    return HttpResponse(json.dumps(ret))




