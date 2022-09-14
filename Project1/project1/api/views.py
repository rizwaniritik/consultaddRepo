from calendar import c
from django.shortcuts import render,redirect
from django.http import HttpResponse,request
import requests
import json
from api.models import Nasa,WhoIs
import configparser
import bs4 as bs
import datetime
import boto3
import ast
import xmltodict
def home(request):
    
    r=requests.get('https://api.nasa.gov/EPIC/api/natural?api_key=zRgiJagbMNtaXlHWHrEL1S874Q4FJmXxHcthnCji')
    data=json.loads(r.content)
   
    # for i in data:
    #     i['version']='1.0.0'
    #     i['date']=i['date'][:10]
    #     p=Nasa.objects.create(identifier=i['identifier'],caption=i['caption'],image=i['image'],version=i['version'],date=i['date'])
    #     p.save()
    context=Nasa.objects.all()
    return render(request,'index.html',{'context':context})



def link(request):
    config=configparser.ConfigParser()
    config.read('/Users/consultadd/Desktop/codes/Project1/project1/api/project1.ini') 
    key=config.get('credentials','key')
    
    if request.method=='POST':
        ip=request.POST.get('ip1')
        
        link="https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=%s&domainName=%s" %(key,ip)
        
        r=requests.get(link)
        file=bs.BeautifulSoup(r.content,'xml')
       
        organization=file.find('organization').text
        state=file.find('state').text
        country=file.find('country').text
        description=file.find('rawText').text[:70]
        creation_date=file.find('createdDate').text[:10]
        cd=creation_date.split('-')
        cd=datetime.date(int(cd[0]),int(cd[1]),int(cd[2]))
        w=WhoIs.objects.create(ip=ip,organization=organization,state=state,country=country,description=description,creation_date=cd)
        w.save()
        jsondict={
        'organization':organization,
        'state':state,
        'country':country,
        'description':description,
        'creation_date':creation_date
        }
        s3=boto3.client('s3')
        
        filedata=s3.get_object(Bucket='ritikbucket102',Key='ritik.json')
       
        
        
        filecontent=filedata["Body"].read().decode('utf-8')
        if len(filecontent)!=0:
            
            filecontent=json.loads(filecontent)
            data=[record for record in filecontent]
            data.append(jsondict)
            data=json.dumps(data)
        else:
            data=json.dumps([jsondict])
        print(data)
        
        

        s3 = boto3.resource('s3')
        bucket = s3.Bucket('ritikbucket102')
        
        object = bucket.put_object(
        ACL='private',
        Body=(str(data)).encode('utf-8'),
        
        Key='ritik.json'
    )
    return render(request,'link.html')
    

def api2(request):
    if request.method=='POST':
        r=requests.get('https://fuf3llej5d.execute-api.us-east-2.amazonaws.com/prod')


    return redirect('link')

# ['identifier', 'caption', 'image', 'version', 'centroid_coordinates', 'dscovr_j2000_position', 'lunar_j2000_position', 'sun_j2000_position', 'attitude_quaternions', 'date', 'coords']