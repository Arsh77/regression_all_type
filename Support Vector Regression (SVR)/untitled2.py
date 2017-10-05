import sys

def timeConversion(s):
    # Complete this function
    b= s.find('PM')
    #print('b = ', b)
    if b!=-1:
        s=s.strip('PM')
        #print('s = ', s)
        y=list(map(int , s.strip().split(':')))
        if y[2]>=0 and y[2] <=59 and y[1]>= 0 and y[1]<=59 and y[0]>=1 and y[0]<=12:
        #print('y = ', y)
            if y[0]==12:
                y[1]= add_zero(y,1)
                y[2]=add_zero(y,2)
                res = str(y[0])+':'+str(y[1])+':'+str(y[2])
            else:
                y[1]= add_zero(y,1)
                y[2]=add_zero(y,2)         
                res =str(y[0]+12)+':'+str(y[1])+':'+str(y[2])     
        else:
            raise Exception('seconds and minute can be between 0 and 59 and hour between 1 and 12')                
    else:
                    
        s=s.strip('AM')
        y=list(map(int , s.strip().split(':')))
        if y[2]>=0 and y[2] <=59 and y[1]>= 0 and y[1]<=59 and y[0]>=1 and y[0]<=12:   
            
            if y[0]==12: 
                y[1]= add_zero(y,1)
                y[2]=add_zero(y,2)
                res='0'+str(y[0]-12)+':'+str(y[1])+':'+str(y[2])
            else:
                y[0]=add_zero(y,0)
                y[1]= add_zero(y,1)
                y[2]=add_zero(y,2)
                res =str(y[0])+':'+str(y[1])+':'+str(y[2])   
        else:
            raise Exception('seconds and minute can be between 0 and 59 and hour between 1 and 12')                
               
    return res            

def add_zero(y , i=0):
    if y[i]>=0 and y[i]<=9:
        y[i]=str('0'+str(y[i]))  
    return(y[i])
    
    
def f(): 
    s = input().strip()
    result = timeConversion(s)
    print(result)
f()


n = input().strip()
if n%2 != 0:
    print('Weird')
if n%2 == 0:
    if n>=2 and n<=5:
        print('Not Weird')
    if n>=6 and n<=20:
        print('Weird')
    if n>20:
        print('Not Weird')








        
ins = input().strip()

is_pm = ins[-2:].lower() == 'pm'
time_list = list(map(int, ins[:-2].split(':')))

if is_pm and time_list[0] < 12:
    time_list[0] += 12

if not is_pm and time_list[0] == 12:
    time_list[0] = 0

print(':'.join(map(lambda x: str(x).rjust(2, '0'), time_list)))


a = input().strip()
b= list(map(int , a.strip().split(' ')))
c = min(b)
d=0
for i in range(c):
    if b[0]%(i+1)==0 and b[1]%(i+1)==0:
        d+=1
print(d)        






a = input().strip()

b= list(map(int , a.strip().split(' ')))

c1 = b[0]
c2 = b[1]
d=0
import math
from fractions import gcd
n = gcd(c1 , c2)
print(n)
for i in range(int(round(math.sqrt(n))+1)):
    print(i)
    if i ==0:
        pass
    else:
        if n%i==0:
            if (n/i)==i:
                d+=1
                print(d)
            else:
                d+=2
                print(d)
print(d)                

import math

n =  input().strip()
list_n=list(map(int , n.strip().split(' ')))

sum_n=sum(list_n)
import numpy as np
avg_n = np.mean(list_n)
q=math.ceil(avg_n)

for x in range(len(list_n)):
    list_n[x]=q
    
print(list_n)        







n = input().strip()
l = input().strip()
ln=list(map(int, l.strip().split(' ')))
sln = int(sum(ln))
n= int(n)
from math import ceil
import numpy as np
if sln % n==0:
    d= int(sln/n)+1
else :   
    d= ceil(np.mean(ln))

print(d)









































    