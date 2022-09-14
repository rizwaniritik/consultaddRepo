from cymruwhois import Client
import socket
import os
import  json
c=Client()
lst1=[]
with open ('/Users/consultadd/Desktop/codes/NetScoutScripts/sites/ibmcloud1.txt','r') as sfile1:
            for line in sfile1:
                dct=json.loads(line)
                lst1.append(dct["block"])
for i in lst1:
    r=c.lookup(i.split('/')[0])
    print(r.owner)
print(r.owner)