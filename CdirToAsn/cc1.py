from cymruwhois import Client
import socket
import os
import  json
c=Client()
lst1=[]
with open ('/Users/consultadd/Desktop/codes/NetScoutScripts/sites/alibaba1.txt','r') as sfile1:
            for line in sfile1:
                lst1.append(str(line))
for i in lst1:
    
    r=c.lookup(i.split('/')[0])
    print(r.owner)
print(r.owner)