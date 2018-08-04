from django.shortcuts import render
from django.templatetags.static import static

import common.common as com
import common.models as models
import analysis.analysis as analysis

# Create your views here.
def number_count(request):
    __startVolume = ""
    __endVolume = ""
    innerTag = ""
    
    if request.POST:
        __startVolume = request.POST['startVolume']
        __endVolume = request.POST['endVolume']
    
        if (__startVolume !="" and __endVolume!=""): 
            imgName = analysis.NumberCount(__startVolume,__endVolume)
            url = static('temp/' + imgName)
            innerTag = "<img src=\""+ url +"\" >"
        else:
            innerTag = "<div style=\"color:red\">期號不得為空！！</div>"
            
    return render(request, 'number_count.html', {'innerTag': innerTag})


def number_grid(request):
    __startVolume = ""
    __endVolume = ""
    __category = "5" #雙贏彩
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

    category = models.category.objects.all().order_by('id')
    return render(request, 'number_grid.html', {'category':category,'innerHtml':innerHtml})











