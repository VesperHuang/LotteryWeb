import sqlite3

__connectionString = ".\lottery.db"
    
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