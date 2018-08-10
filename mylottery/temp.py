# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:33:24 2018

@author: Vepser
"""
import re

list = []
temp_list1 = ["*+32","*+2","*+3","*-4","5","6"]
temp_list2 = [7,8,9,10,11,12]
dic_1 = {"id":1,"name":"vesper","age":"18","list":temp_list1}
dic_2 = {"id":2,"name":"ally","age":"18","list":temp_list2}

list.append(dic_1)
list.append(dic_2)

#print(len(list))
#print(list[0]["list"])

number_1 = list[0]["list"][0]
#print(number_1)
#print(re.match('*-',"*-1").span())


#pattern = re.compile(r'\*\+')  
#m = pattern.match(number_1)
#print(m)
#print(m.group())
#print(type(m))
#
#pattern = re.compile(r'[1-9]') 
#n=re.search(pattern, number_1)
#print(n.group())

#print(re.match('www', 'www.runoob.com').span())

#None
#<class 'NoneType'>

#<_sre.SRE_Match object; span=(0, 2), match='*+'>
#<class '_sre.SRE_Match'>



#pattern = re.compile(r'\*\+')  
#m = pattern.match(number_1)

#if re.match(r'\*\+',number_1) :
#    pattern = re.compile(r'[0-9][0-9]') 
#    n=re.search(pattern, number_1)
#    print("*+ :",n.group())
#    print(type(n.group()))
#elif re.match(r'\*\-',number_1) :
#    pattern = re.compile(r'[0-9][0-9]') 
#    n=re.search(pattern, number_1)
#    print("*- :",str(n.group()))
#    print(type(n.group()))
#else:
#    pattern = re.compile(r'[0-9][0-9]') 
#    n=re.search(pattern, number_1)
#    print(n.group())    
#    print(type(n.group()))

#print(m)
#print(m.group())
#print(type(m))
#

pattern = re.compile(r'\d{1,2}') 
n=re.search(pattern, str(number_1))
print(type(n))
print(n.group())  