from ipwhois import IPWhois
import json
lst1=[]
with open('/Users/consultadd/Desktop/codes/NetScoutScripts/testsites/new.txt','r') as sfile1:
   for line in sfile1:
                dct=json.loads(line)
                lst1.append((dct["block"]).split('/')[0])
   for line in lst1:
   
      obj = IPWhois((str(line)).split('/')[0])
      res=obj.lookup_rdap(asn_methods=["whois"])
      for i in res['objects'].keys():
         print(res['objects'][i]['contact']['name'])
         break