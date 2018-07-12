from bokeh.io import export_png
from bokeh.plotting import figure

import os,shutil
import random
import common.common as com

def NumberCount(startVolume,endVolume):
    sql = ""
    sql = "select * from Two_Win where volume between \'" + startVolume + "\' and \'" + endVolume + "\'"
    rows = com.getTableData(sql)
    
    #建立 1 到 24 字典 做為儲存統計用
    dic = {}
    for i in range(1,25):
        dic.setdefault("no"+ str(i),0)
    
    #統計 1 到 24 出現次數 並存回字點中 
    if(rows != None):
        for row in rows:
    #        print("{}".format(row[0]))
            for j in range(2,14):
                dic["no" + str(row[j])] += 1            
    #print(dic)
    
    #顯示柱狀圖(bokeh) 
    #output_file("bars.html")
    listx = list(dic.keys())
    listy = list(dic.values())
    __title = startVolume +" 期 - "+ endVolume +" 期 號碼次數統計"
    
    p = figure(x_range=listx, plot_height=250, title=__title,
               toolbar_location=None, tools="")
    p.vbar(x=listx, top=listy, width=0.9)
    
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    #show(p)
    
    __filename = str(random.randrange(0,10001,4)) + "-bars.png"
    export_png(p,filename=__filename) #因為想嵌套至其它網頁中 故改成圖檔輸出 方便操做
    
#        cur_path = os.path.dirname(__file__) #取得目前的目錄路徑   
#        print(cur_path)
    file = os.path.abspath(__filename) #傳回檔案完整的路徑名稱
    
    if os.path.exists(file):
        #將檔案移到 static/temp 底下 
        __source_file_path = "C:\\ProgramData\\Anaconda3\\Scripts\\LotteryWeb\\" + __filename
        __target_file_path = "C:\\ProgramData\\Anaconda3\\Scripts\\LotteryWeb\\analysis\\static\\temp\\" + __filename            
        shutil.move(__source_file_path,__target_file_path)            
    return __filename








