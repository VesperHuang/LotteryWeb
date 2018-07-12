from django.shortcuts import render
from django.views.decorators import csrf
import common.common as com
import common.models as models

def mylottery(request):
    mylottery = models.MyLottery.objects.all().order_by('-volume')
    return render(request, "myLottery.html", {'mylottery':mylottery}) 
    
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
    return render(request, "myLottery.html", {'mylottery':mylottery})    