from django.shortcuts import render,HttpResponse

import common.common as com
import common.models as models
import json

#from firebase import firebase
from mylottery.models import users

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

def lottery_compare(request):
    ACTION = "/lottery_compare"
    __category = ""
    __startVolume = ""
    __endVolume = ""

    #post
    if request.POST: 
        if(request.POST['category'] != ""):        
            __category = request.POST['category']
        if(request.POST['startVolume'] != ""):        
            __startVolume = request.POST['startVolume']                                      
        if(request.POST['endVolume'] != ""):        
            __endVolume = request.POST['endVolume']   
        
#        print("category:",__category_post,"startVolume",__startVolume,"endVolume",__endVolume)
        mylottery = models.MyLottery.objects.filter(category = __category,volume__range=[__startVolume,__endVolume]).order_by('-volume')
        
    else:   
        #setp1 get my lottery data filter is category and volume    
        #page load get twowin last 10
        __category = "5"
        mylottery = models.MyLottery.objects.filter(category = __category).order_by('-volume')[:10]
        __startVolume = mylottery[9].volume
        __endVolume = mylottery[0].volume
        
    #setp2 get lotery number filter equal my lottery 
    volumn_number_list = []
    if(__category.isdigit() and __category == "2"):
#        lottery = models.BigLottery.objects.filter(volume = __volume)
        lottery = models.BigLottery.objects.filter(volume__range=[__startVolume,__endVolume])
        for item in lottery:
            number_list=[]
            number_list.append(item.volume)
            number_list.append(item.no1)
            number_list.append(item.no2)
            number_list.append(item.no3)
            number_list.append(item.no4)
            number_list.append(item.no5)
            number_list.append(item.no6)
            number_list.append(item.special)
            volumn_number_list.append(number_list)
        
    elif(__category.isdigit() and __category == "5"):
#        lottery = models.TwoWin.objects.filter(volume = __volume)
        lottery = models.TwoWin.objects.filter(volume__range=[__startVolume,__endVolume])
        for item in lottery:
            number_list = []  
            number_list.append(item.volume)
            number_list.append(item.no1)
            number_list.append(item.no2)
            number_list.append(item.no3)
            number_list.append(item.no4)
            number_list.append(item.no5)
            number_list.append(item.no6)
            number_list.append(item.no7)
            number_list.append(item.no8)
            number_list.append(item.no9)
            number_list.append(item.no10)
            number_list.append(item.no11)
            number_list.append(item.no12)
            volumn_number_list.append(number_list)
        
    #setp3 compare,my lottery loop to check lottery number then markup hit number
    result = []
    for item in mylottery:
        my_number_list = []
        my_lottery_item = {"id":item.id,"volume":item.volume,"date":item.date,"result":my_number_list}    
        
        if(__category.isdigit() and __category == "2"):
            my_number_list.append(item.no1)
            my_number_list.append(item.no2)
            my_number_list.append(item.no3)
            my_number_list.append(item.no4)
            my_number_list.append(item.no5)
            my_number_list.append(item.no6)        
        
        elif(__category.isdigit() and __category == "5"):        
            my_number_list.append(item.no1)
            my_number_list.append(item.no2)
            my_number_list.append(item.no3)
            my_number_list.append(item.no4)
            my_number_list.append(item.no5)
            my_number_list.append(item.no6)  
            my_number_list.append(item.no7)
            my_number_list.append(item.no8)
            my_number_list.append(item.no9)
            my_number_list.append(item.no10)
            my_number_list.append(item.no11)
            my_number_list.append(item.no12)            
        
        for volumn in volumn_number_list:
            if item.volume == volumn[0]:
                for number in volumn[1:]:
                    flag= "false"
                    for my_number in my_number_list:
                        if(number == my_number):
                            my_number_list.remove(my_number)
                            my_number_list.append("*+" + str(number))
                            flag = "true"
                    
                    if(flag == "false"):
                        my_number_list.append("*-" + str(number))
                            
                my_lottery_item['result'] = my_number_list
                result.append(my_lottery_item)
    
    #setp3 create html table tag 
    category_name = com.get_categroy_name(__category)
    category = models.category.objects.filter(switch = 'on').order_by('id')
    innerHtml = "<div> 查詢：" + category_name + " 第 "+__startVolume+" 期 ～ 第 "+__endVolume+" 期 開出號碼</div></br>"
    innerHtml += com.get_compare_table_tag(result,"5")
    return render(request, "lottery_compare.html", {'ACTION':ACTION,'category':category,'innerHtml':innerHtml})   

#def firebase_operate(request):       
##    from firebase_admin import credentials 
##    cred = credentials.Certificate("path/to/serviceAccountKey.json")
##    fb = firebase_admin.initialize_app(cred)    
#    
#    url="https://lottery-web-d3348.firebaseio.com"
##    auth = firebase.FirebaseAuthentication('iHKdPXaSRUVgf8RoZw4xh8gJBk03','deepvesper@gmail.com')
#    fb = firebase.FirebaseApplication(url,None)
#    
## 新增
#    students=[
#            {'no':1,'name':'李天龍'}]
#    
#    for sutdent in students:
#        fb.post('/students',sutdent)
#
## 刪除    
## =============================================================================
##     datas =  fb.get('/students',None)
##     no = 1
##     key_id = CkeckKey(no,datas)
##     fb.delete('/students/' + key_id,None)
##     result = fb.get('/students',None)
## =============================================================================
#    
## 修改
## =============================================================================
##     datas =  fb.get('/students',None)
##     no = 2
##     key_id = CkeckKey(no,datas)
##     data = {"no":int(2),"name":"梁靜茹"}
##     fb.put(url+'/students/',data=data,name=key_id)
## =============================================================================
#    
#    result =  fb.get('/students',None)
#    return render(request, "firebase.html", {'result':result})     

def mylottery(request):
#    mylottery = models.MyLottery.objects.filter(category = 5).order_by('-volume')
#    innerHtml = com.get_table_tag(mylottery)
#    return render(request, "myLottery.html", {'innerHtml':innerHtml}) 
    category = models.category.objects.filter(switch = 'on').order_by('id')
    mylottery = models.MyLottery.objects.filter(category = 2).order_by('-volume')[:10]
    innerHtml = com.get_table_tag(mylottery)
    return render(request, "mylottery.html", {'category':category,'innerHtml':innerHtml})     
    
def mylottery_add(request):
    category = models.category.objects.filter(switch = 'on').order_by('id')
    return render(request, "mylottery-add.html",{'category':category})  
    
def mylottery_adding(request):
    innerHtml =""
    if request.POST:        
        mylottery = models.MyLottery()
        if(request.POST['category'] != ""):
            #類別
            mylottery.category = request.POST['category']
    
        if(request.POST['volume'] != ""):
            #期號
            mylottery.volume = request.POST['volume']
        
        if(request.POST['date'] != ""):
            #開獎日期
            mylottery.date = request.POST['date']

        if(request.POST['number'] != ""):
            numbers = []
            numbers = str(request.POST['number']).split(',')
            
            if(int(request.POST['category']) == 2):
                mylottery.no1 = numbers[0]
                mylottery.no2 = numbers[1]
                mylottery.no3 = numbers[2]
                mylottery.no4 = numbers[3]
                mylottery.no5 = numbers[4]
                mylottery.no6 = numbers[5]     
            elif(int(request.POST['category']) == 5):
                mylottery.no1 = numbers[0]
                mylottery.no2 = numbers[1]
                mylottery.no3 = numbers[2]
                mylottery.no4 = numbers[3]
                mylottery.no5 = numbers[4]
                mylottery.no6 = numbers[5]
                mylottery.no7 = numbers[6]
                mylottery.no8 = numbers[7]
                mylottery.no9 = numbers[8]
                mylottery.no10 = numbers[9]
                mylottery.no11 = numbers[10]
                mylottery.no12 = numbers[11]
            
    mylottery.save()
       
    mylottery = models.MyLottery.objects.filter(category = 5).order_by('-volume')
    innerHtml = com.get_table_tag(mylottery)
    return render(request, "myLottery.html", {'innerHtml':innerHtml})    

def mylottery_add_ajax(request):
    category = models.category.objects.filter(switch = 'on').order_by('id')
    return render(request, "ajax_post.html",{'category':category})     

def ajax_category(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        if(request.method == "POST"):
            category_id = request.POST.get('category')
            print("category_id:",category_id)
            mylottery = models.MyLottery.objects.filter(category = category_id).order_by('-volume')[:10]
            innerHtml = com.get_table_tag(mylottery)
            ret['data'] = innerHtml 
        else:
            ret['status'] = False
            ret['error'] = "攔位不得為空！"           
    except Exception as e:
        ret['status'] = False
        ret['error'] = '請求錯誤'
        
    return HttpResponse(json.dumps(ret))

def ajax_post(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:   
        if(request.method == "POST"):
            category = request.POST.get('category')
            volume = request.POST.get('volume')
            date = request.POST.get('date')
            number = request.POST.get('number')

            if( category != "" and volume != "" and date !="" and number !=""):
                mylottery = models.MyLottery()
                mylottery.category = category
                mylottery.volume = volume
                mylottery.date = date
                
                numbers = []
                numbers = str(number).split(',')
                
                if(int(category) == 2):
                    mylottery.no1 = numbers[0]
                    mylottery.no2 = numbers[1]
                    mylottery.no3 = numbers[2]
                    mylottery.no4 = numbers[3]
                    mylottery.no5 = numbers[4]
                    mylottery.no6 = numbers[5]     
                elif(int(category) == 5):
                    mylottery.no1 = numbers[0]
                    mylottery.no2 = numbers[1]
                    mylottery.no3 = numbers[2]
                    mylottery.no4 = numbers[3]
                    mylottery.no5 = numbers[4]
                    mylottery.no6 = numbers[5]
                    mylottery.no7 = numbers[6]
                    mylottery.no8 = numbers[7]
                    mylottery.no9 = numbers[8]
                    mylottery.no10 = numbers[9]
                    mylottery.no11 = numbers[10]
                    mylottery.no12 = numbers[11]

                mylottery.save()
            else:
                ret['status'] = False
                ret['error'] = "攔位不得為空！"   
    except Exception as e:
        ret['status'] = False
        ret['error'] = '請求錯誤'
        
    return HttpResponse(json.dumps(ret))




