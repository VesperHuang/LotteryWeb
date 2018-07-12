from django.shortcuts import render
from django.templatetags.static import static

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