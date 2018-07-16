from django.shortcuts import render
from django.templatetags.static import static

from common.models import TwoWin
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
            innerHtml += get_table_tag(number_list)
        else:
            innerHtml = "<div style=\"color:red\">期號不得為空！！</div>"
    else:
        number_list = TwoWin.objects.order_by('-volume').all()[:10]
        innerHtml += get_table_tag(number_list)

    return render(request, 'number_grid.html', {'innerHtml':innerHtml})

def get_table_tag(number_list):

    result = ""
    result = "<table style='width:500px;'>"
    
    head = ""
    head += "<tr style='height:20px;'>"
    head += "<td>期 別</br>(日 期)</td>"
    for column in range(1,25):
        head += "<td>no-"+str(column)+"</td>"
    head += "</tr>"
    
    temp = []    
    result += head
    for item in number_list:
        temp.append(item.no1)
        temp.append(item.no2)
        temp.append(item.no3)
        temp.append(item.no4)
        temp.append(item.no5)
        temp.append(item.no6)
        temp.append(item.no7)
        temp.append(item.no8)
        temp.append(item.no9)
        temp.append(item.no10)
        temp.append(item.no11)
        temp.append(item.no12)
    
        result += "<tr style='height:20px;'>"
        result +="<td>"+ item.volume +"</br>("+ item.date +")</td>"
        for column in range(1,25):
            flag = "false"
            for value in temp:
                if (column == value):
                    result += "<td>"+ str(value) +"</td>"
                    flag = "true"
                    temp.remove(value)
            if(flag == "false"):
                result += "<td> </td>"
    
        result +="<tr>"  
        temp.clear()
    result += "</table>"
    return result










