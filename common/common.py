import sqlite3
import re
__connectionString = ".\lottery.db"


category_dic = {
        "2":49,
        "5":24}
    
def myName(name):
    return "我的名字是" + name

def FormatDate(vDate):
    temp = []
    temp = vDate.split('/')
    
    result = ""
    for i in range(0,len(temp)):
        result += str("{:0>2d}".format(int(temp[i])))
        if( i != len(temp)-1):
            result += "/"
    return result

def ExeSql(vSql):
    conn = sqlite3.connect(__connectionString) #建立資料庫連線
    cursor = conn.cursor() #建立 cursor 物件
    cursor.execute(vSql)
#    print(vSql)
    conn.commit()#主動更新
    conn.close()#關閉資料庫連線
        
def ExeSqls(vSql):    
    conn = sqlite3.connect(__connectionString) #建立資料庫連線
    cursor = conn.cursor() #建立 cursor 物件    
    for k in range(0,len(vSql)):
        cursor.execute(vSql[k])
#        print(vSql[k])
    conn.commit()#主動更新
    conn.close()#關閉資料庫連線    
    
    
def getTableData(vSql):
    conn = sqlite3.connect(__connectionString)
    cursor = conn.execute(vSql)
    result = cursor.fetchall()     
#    print(result)
    conn.close()#關閉資料庫連線
    return result

def get_categroy_name(index):
    result = ""
    if(index == "1"):  
        result = "威力彩"
    elif(index == "2"):
        result = "大樂透"
    elif(index == "3"):
        result = "大福彩"        
    elif(index == "4"):
        result = "今彩539"        
    elif(index == "5"):
        result = "雙贏彩"        
    elif(index == "6"):
        result = "BINGO BINGO賓果賓果"      
    elif(index == "7"):
        result = "3星彩"      
    elif(index == "8"):
        result = "4星彩"      
    elif(index == "9"):
        result = "38樂合彩"              
    elif(index == "10"):
        result = "49樂合彩"      
    elif(index == "11"):
        result = "39樂合彩"   
        
    return result

def get_table_tag(lottery,category=""):

    __category = ""
    result = ""
    result = "<table style='width:100%;'>"
    
    head = ""
    head += "<tr style='height:20px;'>"
    head += "<td width='20px'>期 別</br>(日 期)</td>"
    
    if(category != ""):
        range_max = category_dic[category] + 1 
        __category = category
    else:
        range_max = category_dic[lottery[0].category] + 1
        __category = lottery[0].category
      
    for column in range(1,range_max):
        head += "<td width='20px'>"+str(column)+"</td>"
    head += "</tr>"
    
    temp = []    
    result += head
    
    for item in lottery:
        __special = 0
        if(__category == "2"):
            temp.append(item.no1)
            temp.append(item.no2)
            temp.append(item.no3)
            temp.append(item.no4)
            temp.append(item.no5)
            temp.append(item.no6)
            if(category != ""):
                temp.append(item.special)
                __special = item.special
            
        if(__category == "5"):
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
        for column in range(1,range_max):
            flag = "false"
            for value in temp:
                if (column == value):
                    if(__special != 0 and __special == value):
                        result += "<td style = 'background-color:red;'>"+ str(value) +"</td>"
                    else:
                        result += "<td>"+ str(value) +"</td>"
                    flag = "true"
                    temp.remove(value)
            if(flag == "false"):
                result += "<td> </td>"
    
        result +="<tr>"  
        temp.clear()
    result += "</table>"
    return result

def get_compare_table_tag(lottery,category=""):

    __category = ""
    result = ""
    result = "<table style='width:100%;'>"
    
    head = ""
    head += "<tr style='height:20px;'>"
    head += "<td width='20px'>期 別</br>(日 期)</td>"
    
    if(category != ""):
        range_max = category_dic[category] + 1 
        __category = category
      
    for column in range(1,range_max):
        head += "<td width='20px'>"+str(column)+"</td>"
    head += "</tr>"

    result += head
    for item in lottery:
        result += "<tr style='height:20px;'>"
        result +="<td>"+ item["volume"] +"</br>("+ item["date"] +")</td>"
        for column in range(1,range_max):
            flag = "false"
            for value in item["result"]:
                color = ""
                number = ""
                
                if re.match(r'\*\+',str(value)) :
                    pattern = re.compile(r'\d{1,2}') 
                    n=re.search(pattern, value)
                    
                    color = "red"
                    number = n.group()
                elif re.match(r'\*\-',str(value)) :
                    pattern = re.compile(r'\d{1,2}') 
                    n=re.search(pattern, str(value))  
                    
                    color = "yellow"
                    number = n.group()                    
                else:
                    pattern = re.compile(r'\d{1,2}') 
                    n=re.search(pattern, str(value))

                    color = ""
                    number = n.group()  
                    
                if str(column) == number :
                    if color != "" :
                        print("column:",column,"number",number)
                        result += "<td style = 'background-color:"+ color+";'>"+ number +"</td>"
                    else:
                       result += "<td style = 'background-color:gray'>"+ number +"</td>" 
                    flag = "true"                       

            if flag == "false":
                result += "<td> </td>" 
         
        result +="<tr>"  
    result += "</table>"
    result += "<div>紅色：命中，黃色：開出，灰色：未中</div>"
    return result