from cymruwhois import Client
import socket
import os
import  json
c=Client()

def cidrToAsn(file,filename):
        lst1=[]
        lst2=[]
        with open (file,'r') as sfile1:
            for line in sfile1:
                dct=json.loads(line)
                lst1.append(dct["block"])
        count1=0
        count2=0
        print(filename[:-5])
        for i in lst1:
           try:
                r=c.lookup((i.split('/'))[0])
            
                if str(filename[:-5]) in (r.owner).lower():
                    count1+=1
                
           except Exception as e:
            print(e)  
            print(i[:-3])
        print(count1,len(lst1)-count1)
        return count1,len(lst1)-count1

if __name__=='__main__':
    directory='/Users/consultadd/Desktop/codes/NetScoutScripts/sites'
    files= os.listdir(directory)
    files.sort()
    with open('/Users/consultadd/Desktop/codes/NetScoutScripts/commonasn.txt','a+') as f:
        for i in files:
            file=os.path.join(directory,i)
            common,uncommon=cidrToAsn(file,i)
            f.write("{'common':%s,'uncommon':%s,'file':%s}\n" %(common,uncommon,i))
