from django.shortcuts import render
from django.templatetags.static import static
from common.models import TwoWin

import common.common as com
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
    innerHtml = ""
    
    if request.POST:
        __startVolume = request.POST['startVolume']
        __endVolume = request.POST['endVolume']
    
        if (__startVolume !="" and __endVolume!=""): 
            number_list = TwoWin.objects.filter(volume__range=[__startVolume,__endVolume]).order_by('-volume')
            innerHtml = "<div> 查詢： 第 "+__startVolume+" 期 ～ 第 "+__endVolume+" 期 開出號碼</div></br>"
            innerHtml += com.get_table_tag(number_list)
        else:
            innerHtml = "<div style=\"color:red\">期號不得為空！！</div>"
    else:
        number_list = TwoWin.objects.order_by('-volume').all()[:10]
        innerHtml += com.get_table_tag(number_list)

    return render(request, 'number_grid.html', {'innerHtml':innerHtml})











