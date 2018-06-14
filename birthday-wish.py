import httplib, urllib 
import os 
import json 
import time 
import calendar 
  
access_token=""
dob='2013-04-24'
conn = httplib.HTTPSConnection("Page on Facebook") 
print 'requesting...'

has_more=False
def convert_to_local(s): 
    t=time.strptime(s[:19],"%Y-%m-%dT%H:%M:%S") 
    t=time.localtime(calendar.timegm(t)) 
    t=time.strftime("%Y-%m-%d",t) 
    return t 
  
def getRandomThnx(msg): 
    return 'thanks :)'
    
def process_posts(url): 
    conn = httplib.HTTPSConnection("Page on Facebook") 
    conn.request("GET",url) 
    res = conn.getresponse() 
    conn.getresponse 
    data=res.read() 
    res_obj=json.loads(data) 
    posts=res_obj["data"] 
    processed=0
    for post in posts:         
        if not "message" in post: 
            continue
        msg=post["message"] 
        post_date=convert_to_local(post["created_time"])         
        if dob == post_date:             
            if "from" in post and "message" in post:                 
                user= post["from"]["name"] 
                  
                  
                path='/'+post['id']+'/comments'
                param_data={  'format':'json', 
                        'message':getRandomThnx(msg), 
                        'access_token':access_token 
                      } 
                conn = httplib.HTTPSConnection("Page on Facebook") 
                if post["comments"]["count"]==0: 
                    print 'responding to :'+user+'->'+msg 
                    conn.request("POST",path,urllib.urlencode(param_data),{}) 
                    res = conn.getresponse() 
                path='/'+post['id']+'/likes'
                param_data={  'format':'json', 
                        'access_token':access_token 
                      } 
                  
                conn = httplib.HTTPSConnection("Page on Facebook") 
                processed+=1
  
    if "paging" in res_obj:         
        return processed+process_posts(res_obj["paging"]["next"][len("Page on page on Facebook"):]) 
    else: 
        print "Finished"
        return processed     
url='/me/feed?access_token='+access_token 
print 'total='+str(process_posts(url)) 
print 'Thanx to all wisher :)'
