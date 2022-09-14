__author__=''
__version__='1.0'

import json
import os
from cymruwhois import Client
import socket

class CidrDifference:
    def cdir_difference(self,file1,file2):
        lst1=[]
        lst2=[]
        with open (file1,'r') as sfile1:
            for line in sfile1:
                dct=json.loads(line)
                lst1.append(dct["block"])
        with open (file2,'r') as sfile2:
            for line in sfile2:
                dct=json.loads(line)
                lst2.append(dct["block"])
        c=Client()
        ip=lst1[0][:-3]
        r=c.lookup(ip)
        
        
        a=set(lst1)
        b=set(lst2)
        
        return a^b,a&b,r.owner

        

if __name__=='__main__':
    obj=CidrDifference()
    
    directory='/Users/consultadd/Desktop/codes/NetScoutScripts/testsites'
    files= os.listdir(directory)
    files.sort()
    with open('/Users/consultadd/Desktop/codes/NetScoutScripts/metrics.txt','w+') as f:
        for i in range(0,len(files),2):
            file1=os.path.join(directory,files[i])
            file2=os.path.join(directory,files[i+1])
            dissimilar,similar,owner=obj.cdir_difference(file1,file2)
            f.write("{'site':'%s','similar':%s,'dissimilar':%s,'asn':'%s'}\n" %(files[i],len(similar),len(dissimilar),owner))