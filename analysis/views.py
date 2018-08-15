from django.shortcuts import render
from django.templatetags.static import static
import datetime

import common.common as com
import common.models as models
import analysis.analysis as analysis


# Create your views here.
def number_count(request):
    ACTION = "/number_count"
    __category = "5" #雙贏彩
    __startVolume = ""
    __endVolume = ""
    innerHtml = ""
    
    if request.POST:
        __category = request.POST['category']
        __startVolume = request.POST['startVolume']
        __endVolume = request.POST['endVolume']
        
        if (__category !="" and __startVolume !="" and __endVolume!=""): 
            innerHtml = analysis.NumberCount(__category,__startVolume,__endVolume)
#            print(innerHtml)
#            imgName = analysis.NumberCount(__category,__startVolume,__endVolume)
#            url = static('temp/' + imgName)
#            innerHtml = "<img src=\""+ url +"\" >"
            
#            20180813 add record user search log
            user_search_log = models.user_search_log()
            user_search_log.user_name = request.session['user_name'] 
            user_search_log.active = ACTION
            user_search_log.condiction = "'category':'" + __category + "','startVolume':'" + __startVolume +"','endVolume':'"+__endVolume+"'"
            user_search_log.result = innerHtml
            user_search_log.date_time = datetime.datetime.now()
            user_search_log.save()
        else:
            innerHtml = "<div style=\"color:red\">條件不得為空！！</div>"
    else:
        if (request.session.get('user_name',False) ):
            user_search_log = models.user_search_log.objects.filter(user_name = request.session['user_name'] ).order_by('-id')[:1]
            innerHtml = user_search_log[0].result       
    
    category = models.category.objects.filter(switch = 'on').order_by('id')        
    return render(request, 'number_count.html', {'ACTION':ACTION,'category':category,'innerHtml': innerHtml})

def number_grid(request):
    ACTION = "/number_grid"
    __category = "5" #雙贏彩
    __startVolume = ""
    __endVolume = ""
    category_name = com.get_categroy_name(__category)
    innerHtml = ""
    
    if request.POST:
        __category = request.POST['category']
        category_name = com.get_categroy_name(__category)
        __startVolume = request.POST['startVolume']
        __endVolume = request.POST['endVolume']
    
        if (__category != "" and __startVolume !="" and __endVolume!=""): 
#            model = null
            if (__category == "2"):
                model = models.BigLottery
            elif(__category == "5"):
                model = models.TwoWin
           
            number_list = model.objects.filter(volume__range=[__startVolume,__endVolume]).order_by('-volume')
            
            innerHtml = "<div> 查詢：" + category_name + " 第 "+__startVolume+" 期 ～ 第 "+__endVolume+" 期 開出號碼</div></br>"
            innerHtml += com.get_table_tag(number_list,__category)
        else:
            innerHtml = "<div style=\"color:red\">期號不得為空！！</div>"
    else:
        number_list = models.TwoWin.objects.order_by('-volume').all()[:10]
        innerHtml = "<div>" + category_name + " 近10期 開出號碼</div></br>"
        innerHtml += com.get_table_tag(number_list,__category)

    category = models.category.objects.filter(switch = 'on').order_by('id')
    return render(request, 'number_grid.html', {'ACTION':ACTION,'category':category,'innerHtml':innerHtml})











