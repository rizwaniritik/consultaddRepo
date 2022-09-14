from ipwhois import IPWhois
import os
import json

def owner(ip):
    try:
        obj = IPWhois(ip)
        res=obj.lookup_rdap(asn_methods=["whois"])

        for i in res['objects'].keys():
            return res['objects'][i]['contact']['name']
    except:
        return ''

def cidrToAsn(file):
        lst1=[]
        lst2=[]
        with open (file,'r') as sfile1:
            for line in sfile1:
                dct=json.loads(line)
                lst1.append((dct["block"]).split('/')[0])
        for i in lst1:
            lst2.append(owner(i))
        return lst2




if __name__=='__main__':
    directory='/Users/consultadd/Desktop/codes/NetScoutScripts/sites'
    files= os.listdir(directory)
    files.sort()
    with open('/Users/consultadd/Desktop/codes/NetScoutScripts/final.txt','w+') as f:
        for i in files:
            file=os.path.join(directory,i)
            asns=cidrToAsn(file)
            f.write("%s %s %s %s" %(asns.count(asns[0]),len(asns),asns[0],'\n\n'))
