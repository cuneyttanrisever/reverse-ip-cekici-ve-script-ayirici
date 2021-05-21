#!/usr/bin/python
#-*-coding:utf-8-*-
import os
import requests
import re
import sys
import socket
from bs4 import BeautifulSoup
import urllib2
import ssl
import time
os.system('cls' if os.name == 'nt' else 'clear')
reload(sys) 
sys.setdefaultencoding('utf-8')
class renkler:
    HEADER = '\033[95m'
    mavi = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    kirmizi = '\033[91m'
    beyaz = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print renkler.yesil + """
#######################################################
#               Hacked by DexmoD                      #
#         Reverse ip Cekeici :*)                      #
#         Kullanimi : google.com enter                #
#         seklinde yaziniz. Http vs kullanmayiniz.    #
#         Yalniz domaini yaziniz.                     #
#######################################################
"""

print "basladi"
sor=raw_input("url gir basinda http olmasin = ")
v=[]
vv=[]
vvv=[]
vvvv=[]
sonv=[]
try:
    if "http" in sor:
        print renkler.kirmizi+"iyi bir sonuc icin http veya https yazma"+renkler.beyaz
        sys.exit()
    addr1 = socket.gethostbyname(sor) 
    print str(addr1)+"\n"
    urlcik="http://viewdns.info/reverseip/?host=%s&t=1"%(str(addr1))


    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    request = rq.get(urlcik,timeout=10)
    c= request.content
    soup= BeautifulSoup(c,'html.parser')
    kb= soup.findAll("td")
    for i in kb:
        c=re.match("<td>+.*</td>",str(i))
        if c:
            vv.append(c.group())
    for i in vv[4:]:
        k=i.replace("<td>","")
        vvv.append(k)
    for i in vvv:
        k=i.replace("</td>","")
        vvvv.append(k)
    for i in vvvv:
        cc=open("urller.txt","a")
        cc.write(i+"\n")
        cc.close()
        print str(i)+"\n"
except socket.gaierror:
    print renkler.kirmizi+"url bulunamadi atlaniyor..."+renkler.beyaz
                
v=[]
vv=[]
vvv=[]
vvvv=[]
sonv=[]
print renkler.yesil+"urller.txt dosyasina yazilmistir.\nAyni urller dosyadan silinmistir.\nScript ayirma islemi baslatilmistir."+renkler.beyaz
urlist= open("urller.txt","r").readlines()
deli=[]
deli1=[]
deli3=[]
for dexmod in urlist:
    dex=dexmod.replace("\n","")
    deli.append(dex)
for kar in deli:
    if deli1.count(kar)==0:
        deli1.append(kar)
urlist= open("urller.txt","w")
urlist.close()
for delic in deli1:
    urlist= open("urller.txt","a")
    urlist.write(delic+"\n")
    urlist.close()
deli=[]
deli1=[]
deli3=[]

dosya=open("joomla.txt","w")
dosya.close()
dosya=open("wordpress.txt","w")
dosya.close()
dosya=open("drupal.txt","w")
dosya.close()
dosya=open("vbulletin.txt","w")
dosya.close()
dosya=open("mybb.txt","w")
dosya.close()
dosya=open("phbb.txt","w")
dosya.close()
dosya=open("opencart.txt","w")
dosya.close()
dosya=open("xenforo.txt","w")
dosya.close()

jom=[]
wordp=[]
drup=[]
vbull=[]
phpb=[]
opencard=[]
xenfor=[]
urlist= open("urller.txt","r").readlines()
for url1 in urlist:
    url2= url1.replace("\n","")
    print url2
    urld='http://'
    urlt=urld+url2
    print urlt
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) 
    try:
        info = urllib2.urlopen(urlt, context=gcontext).read()  
        info3 = urllib2.urlopen(urlt, context=gcontext)
        vc= info3.geturl()
        
        soup= BeautifulSoup(info, "html.parser")
        
        for wp  in soup:
            if re.findall("/wp-content/" and "/wp-includes/" and "xmlrpc.php" , str(wp)):
                print "wp bulundu  = "+ urlt
                p=open("wordpress.txt","a")
                p.write(vc+"\n")
                wordp +=1
             
            elif re.findall("Joomla! - Open Source Content Management" and "Joomla!" and "/templates/"  , str(wp)):
                print "joomla  ="+ urlt
                p=open("joomla.txt","a")
                p.write(vc+"\n")
                jom +=1
               
            elif re.findall("Drupal - Open Source CMS" and "Drupal" and "/node/" and "/sites/all/themes/"  , str(wp)):
                print "drupal  ="+ urlt
                p=open("drupal.txt","a")
                p.write(vc+"\n")
                drup+=1
               
            elif re.findall("vBulletin" and "vbulletin" and "vBulletin®"   , str(wp)):
                print "vbulletin  ="+ urlt
                p=open("vbulletin.txt","a")
                p.write(vc+"\n")
                vbull +=1
             
            elif re.findall("phpBB" and "phpBB Group"  , str(wp)):
                print "phpbb  ="+ urlt
                p=open("phpbb.txt","a")
                p.write(vc+"\n")
                phpb +=1
              
            elif re.findall("OpenCart" and "index.php?route="  , str(wp)):
                print "OpenCart  ="+ urlt
                p=open("opencart.txt","a")
                p.write(vc+"\n")
                opencard +=1
              
            elif re.findall("XenForo" and "xenforo"   , str(wp)):
                print "OpenCart  ="+ urlt
                p=open("xenforo.txt","a")
                p.write(vc+"\n")
                xenfor +=1
                
    except urllib2.URLError:
        print "baglanmadi"
        continue
    except urllib2.HTTPError:
        print "baglanmadi"
        continue
    except httplib.BadStatusLine:
        print "baglanmadi"
        continue
print renkler.kirmizi+""" 
%s tane wordpress sitesi bulundu. \n
%s tane joomla sitesi bulundu. \n
%s tane drupal sitesi bulundu. \n
%s tane vbulletin sitesi bulundu.\n
%s tane phpbb sitesi bulundu. \n
%s tane opencard sitesi bulundu. \n
%s tane xenforo sitesi bulundu. \n
""" %(wordp,jom,drup,vbull,phpb,opencard,xenfor) +renkler.beyaz
    
