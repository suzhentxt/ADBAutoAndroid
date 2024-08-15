
import os
import cv2
import numpy
import base64
import subprocess
import random
import time
import datetime
from lxml import html


class ADB:
    KEYCODE_0 = 0
    KEYCODE_SOFT_LEFT = 1
    KEYCODE_SOFT_RIGHT = 2
    KEYCODE_HOME = 3
    KEYCODE_BACK = 4
    KEYCODE_CALL = 5
    KEYCODE_ENDCALL = 6
    KEYCODE_0_ = 7
    KEYCODE_1 = 8
    KEYCODE_2 = 9
    KEYCODE_3 = 10
    KEYCODE_4 = 11
    KEYCODE_5 = 12
    KEYCODE_6 = 13
    KEYCODE_7 = 14
    KEYCODE_8 = 0xF
    KEYCODE_9 = 0x10
    KEYCODE_STAR = 17
    KEYCODE_POUND = 18
    KEYCODE_DPAD_UP = 19
    KEYCODE_DPAD_DOWN = 20
    KEYCODE_DPAD_LEFT = 21
    KEYCODE_DPAD_RIGHT = 22
    KEYCODE_DPAD_CENTER = 23
    KEYCODE_VOLUME_UP = 24
    KEYCODE_VOLUME_DOWN = 25
    KEYCODE_POWER = 26
    KEYCODE_CAMERA = 27
    KEYCODE_CLEAR = 28
    KEYCODE_A = 29
    KEYCODE_B = 30
    KEYCODE_C = 0x1F
    KEYCODE_D = 0x20
    KEYCODE_E = 33
    KEYCODE_F = 34
    KEYCODE_G = 35
    KEYCODE_H = 36
    KEYCODE_I = 37
    KEYCODE_J = 38
    KEYCODE_K = 39
    KEYCODE_L = 40
    KEYCODE_M = 41
    KEYCODE_N = 42
    KEYCODE_O = 43
    KEYCODE_P = 44
    KEYCODE_Q = 45
    KEYCODE_R = 46
    KEYCODE_S = 47
    KEYCODE_T = 48
    KEYCODE_U = 49
    KEYCODE_V = 50
    KEYCODE_W = 51
    KEYCODE_X = 52
    KEYCODE_Y = 53
    KEYCODE_Z = 54
    KEYCODE_COMMA = 55
    KEYCODE_PERIOD = 56
    KEYCODE_ALT_LEFT = 57
    KEYCODE_ALT_RIGHT = 58
    KEYCODE_SHIFT_LEFT = 59
    KEYCODE_SHIFT_RIGHT = 60
    KEYCODE_TAB = 61
    KEYCODE_SPACE = 62
    KEYCODE_SYM = 0x3F
    KEYCODE_EXPLORER = 0x40
    KEYCODE_ENVELOPE = 65
    KEYCODE_ENTER = 66
    KEYCODE_DEL = 67
    KEYCODE_GRAVE = 68
    KEYCODE_MINUS = 69
    KEYCODE_EQUALS = 70
    KEYCODE_LEFT_BRACKET = 71
    KEYCODE_RIGHT_BRACKET = 72
    KEYCODE_BACKSLASH = 73
    KEYCODE_SEMICOLON = 74
    KEYCODE_APOSTROPHE = 75
    KEYCODE_SLASH = 76
    KEYCODE_AT = 77
    KEYCODE_NUM = 78
    KEYCODE_HEADSETHOOK = 79
    KEYCODE_FOCUS = 80
    KEYCODE_PLUS = 81
    KEYCODE_MENU = 82
    KEYCODE_NOTIFICATION = 83
    KEYCODE_APP_SWITCH = 187
    KEYCODE_CTRL_LEFT = 113

    def __init__(self, uid) -> None:
        self.uid = uid

    def GetDevices(self):
        listdevice = []
        devices = str(subprocess.check_output("adb devices", shell=True)).replace(
            "b'List of devices attached\\r\\n", '').replace("'", '').replace('bList of devices attached ', '').split('\\r\\n')
        for device in devices:
            if device != '':
                listdevice.append(device.split('\\tdevice')[0])
        return listdevice

    def OpenUrl(self,  url):
        subprocess.call(
            f"adb -s {self.uid} shell am start -a android.intent.action.VIEW -d {url}", shell=True)
        
    def OpenApp(self,  package):
        subprocess.call(
            f"adb -s {self.uid} shell monkey -p {package} -c android.intent.category.LAUNCHER 1", shell=True)
    
    def KillAllApp(self):
        subprocess.check_call(
            f"adb -s {self.uid} shell input keyevent KEYCODE_APP_SWITCH", shell=True)
        time.sleep(1)
        for _ in range(4):
            self.Swipe( x1=800, y1=500, x2=100, y2=500)
            time.sleep(0.2)
        
    def OpenAccountsSetting(self):
        subprocess.check_call(
            f"adb -s {self.uid} shell am start -a android.settings.SYNC_SETTINGS", shell=True)
    
    def CreateFolder(self):
        subprocess.check_call(
            f"adb -s {self.uid} shell mkdir '/sdcard/DCIM/lt'", shell=True)
    
    def DeleteFolder(self):
        subprocess.check_call(
            f"adb -s {self.uid} shell  rm -r '/sdcard/DCIM/lt'", shell=True)

    def PushFile(self,  pathpc, pathphone):
        subprocess.check_call(
            f'adb -s {self.uid} push "{pathpc}" "{pathphone}"', shell=True)
        
    def PushVideo(self,  pathpc):
        try:
            self.DeleteFolder()
        except:
            pass
        
        try:
            self.CreateFolder()
        except:
            pass
        
        subprocess.check_call(
            f'adb -s {self.uid} push "{pathpc}" "/sdcard/DCIM/lt"', shell=True)
        
    
    def ReloadGallery(self):
        subprocess.check_call(
            f'adb -s {self.uid} shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard/DCIM', shell=True)
    
    def ReloadGallery2(self,  file_name):
        subprocess.check_call(
            f'adb -s {self.uid} shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/lt/{file_name}', shell=True) 
    
    def UpdateTimeFile(self,  file_name):
        
        # Lấy thời gian hiện tại
        now = datetime.datetime.now()

        # Định dạng thời gian thành YYYYMMDDHHMM.SS
        current_time = now.strftime("%Y%m%d%H%M.%S")

        subprocess.check_call(f'adb -s {self.uid} shell touch -t {current_time} /sdcard/DCIM/lt/{file_name}')

    def InstallApp(self,  path):
        subprocess.check_call(
            f"adb -s {self.uid} -e install {path}", shell=True)

    def GetApk(self,  package):
        path = subprocess.check_output(
            f"adb -s {self.uid} shell pm path {package}", shell=True).split('\n')
        if path == ['']:
            return
        path = path[0].replace('package:', '')
        subprocess.check_call(
            f"adb -s {self.uid} pull {path} {package}.apk", shell=True)

    def KeyEvent(self,  key):
        subprocess.check_call(
            f"adb -s {self.uid} shell input keyevent {str(key)}", shell=True)

    def CLEAR_TEXT(self,  a, b):
        for _ in range(a):
            subprocess.check_call(
                f"adb -s {self.uid} shell input keyevent 112", shell=True)
        for _ in range(b):
            subprocess.check_call(
                f"adb -s {self.uid} shell input keyevent 67", shell=True)
        
    def InpuText(self,  text=None, VN=None):
        if text == None:
            text = str(base64.b64encode(VN.encode('utf-8')))[1:]
            subprocess.check_call(
                f"adb -s {self.uid} shell ime set com.android.adbkeyboard/.AdbIME", shell=True)
            subprocess.check_call(
                f"adb -s {self.uid} shell am broadcast -a ADB_INPUT_B64 --es msg {text}", shell=True)
            return
        subprocess.check_call(
            f"adb -s {self.uid} shell input text '{text}'", shell=True)

    def Swipe(self,  x1, y1, x2, y2):
        subprocess.check_call(
            f"adb -s {self.uid} shell input touchscreen swipe {x1} {y1} {x2} {y2}", shell=True)
    
    def Swipe_delay(self,  x1, y1, x2, y2, time):
        subprocess.check_call(
            f"adb -s {self.uid} shell input touchscreen swipe {x1} {y1} {x2} {y2} {time}", shell=True)

    def OpenLink(self,  link):
        subprocess.call(
            "adb -s "+self.uid+" shell am start -a android.intent.action.VIEW -d '"+link+"'", shell=True)

    def StopApp(self,  package):
        subprocess.call("adb -s "+self.uid +
                        f" shell am force-stop {package}", shell=True)

    def ScreenCaptureNoSave(self):
        pipe = subprocess.Popen(
            "adb exec-out screencap -p", stdout=subprocess.PIPE, shell=True)
        img_bytes = pipe.stdout.read()
        img = cv2.imdecode(numpy.frombuffer(
            img_bytes, numpy.uint8), cv2.IMREAD_COLOR)
        return img
    
    def ScreenCaptureNoSave1(self):
        name = self.uid
        if ":" in self.uid:
            name = self.uid.replace(":", "").replace(".", "")
        subprocess.check_call(
            f"adb -s {self.uid} shell screencap /sdcard/Download/{name}.png", shell=True)

    def ScreenCapture(self):
        name = self.uid
        if ":" in self.uid:
            name = self.uid.replace(":", "").replace(".", "")
        subprocess.check_call(
            f"adb -s {self.uid} shell screencap /sdcard/Download/{name}.png", shell=True)
        subprocess.check_call(
            f"adb -s {self.uid} pull /sdcard/Download/{name}.png {name}.png", shell=True)
        return f"{name}.png"

    def Pull(self,  path):
        subprocess.check_call(f"adb -s {self.uid} pull {path}", shell=True)

    def Push(self,  path, path1):
        subprocess.check_call(
            f"adb -s {self.uid} push {path} {path1}", shell=True)

    def Click(self,  x, y):
        subprocess.check_call(
            f"adb -s {self.uid} shell input tap {int(x)} {int(y)}", shell=True)

    def FindImg(self,  target_pic_name, time_wait):
        for _ in range(time_wait):
            try:
                img = cv2.imread(target_pic_name)
                img2 = cv2.imread(self.ScreenCapture())
                w, h = img.shape[1], img.shape[0]
                result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
                location = numpy.where(result >= 0.6)
                data = list(zip(*location[::-1]))
                is_match = len(data) > 0
                if is_match:
                    x, y = data[0][0], data[0][1]
                    return x + int(w/2), y + int(h/2)
                else:
                    time.sleep(1)
            except:
                time.sleep(1)
        return False, False
            

    def Grant(self,  package, grant):
        subprocess.check_call(
            f'adb -s {self.uid} shell pm grant {package} android.permission.'+grant)

    def TapImg(self,  img_path, time_wait):
        x, y = self.FindImg( target_pic_name=img_path, time_wait= time_wait)
        if x:
            self.Click( x, y)
            print("Đã tap vào ",x,y)
            return x, y
        return False

    def Change_Proxy(self,  proxy):
        subprocess.check_call(
            f"adb -s {self.uid} shell settings put global http_proxy {proxy}", shell=True)

    def Remove_Proxy(self):
        subprocess.check_call(
            f"adb -s {self.uid} shell settings put global http_proxy :0", shell=True)

    def DeleteCache(self,  package):
        try:
            subprocess.check_output(
                f"adb -s {self.uid} shell pm clear {package}", shell=True)
        except:
            pass

    def SetTextClipbroad(self,  text):
        subprocess.check_call(
            f'adb -s {self.uid} shell am broadcast -a clipper.set -e text "{text}"', shell=True)

    def Paste(self):
        subprocess.check_call(
            f"adb -s {self.uid} shell input keyevent 279", shell=True)

    def DumXml(self):
        name = self.uid
        try:
            os.remove(f"xml/{name}.xml")
        except:
            pass
        if ":" in self.uid:
            name = self.uid.replace(":", "").replace(".", "")
        subprocess.check_call(
            f"adb -s {self.uid} shell uiautomator dump", shell=True)
        print(f'đã dump')
        subprocess.check_call(
            f"adb -s {self.uid} pull /sdcard/window_dump.xml xml/{name}.xml", shell=True)
        return f'xml/{name}.xml'

    def GetPosXml(self,  xpath):
        pos = []
        try:
            path = self.DumXml()
            if not os.path.exists(path):
                return pos
            tree = html.parse(path)
            for bound in tree.xpath(xpath):
                gg = bound.attrib['bounds'].split('][')[
                    0].replace('[', '').split(',')
                pos.append(tuple([int(gg[0]), int(gg[1])]))
            return pos
        except:
            return pos
    
    def FindPosXml(self,  xpath, time_wait):
        print(xpath)
        pos = []
        for _ in range(time_wait):
            try:
                path = self.DumXml()
                if not os.path.exists(path):
                    time.sleep(1)
                else:
                    tree = html.parse(path)
                    for bound in tree.xpath(xpath):
                        gg = bound.attrib['bounds'].split('][')[
                            0].replace('[', '').split(',')
                        pos.append(tuple([int(gg[0]), int(gg[1])]))
                    if pos != []:
                        return pos
                    else:
                        time.sleep(1)
            except:
                time.sleep(1)
        return pos
        
    
    def GetValueByAttrib(self,  xpath, attrib, time_wait):
        value = []
        for _ in range(time_wait):
            try:
                path = self.DumXml()
                if not os.path.exists(path):
                    time.sleep(1)
                else:
                    tree = html.parse(path)
                    elements = tree.xpath(xpath)
                    print("elements:   ", elements)
                    if elements != []:
                        for element in elements:
                            gg = element.attrib[attrib]
                            if gg:
                                value.append(gg)
                        return value
                    else:
                        time.sleep(1)
            except:
                time.sleep(1)
        return value
    
    def GetValueByAttribs(self,  xpath, attribs, time_wait):
        value = []
        for _ in range(time_wait):
            try:
                path = self.DumXml()
                if not os.path.exists(path):
                    time.sleep(1)
                else:
                    tree = html.parse(path)
                    elements = tree.xpath(xpath)
                    print("elements:   ", elements)
                    if elements != []:
                        for element in elements:
                            for attrib in attribs:
                                gg = element.attrib[attrib]
                                if gg != "":
                                    value.append(gg)
                                    return value
                    else:
                        time.sleep(1)
            except:
                time.sleep(1)
        return value
        

    def TapXml(self,  xpath, time_wait , index=0, x=0, y=0):
        for _ in range(time_wait):
            pos = self.GetPosXml( xpath)
            print("pos:  ", xpath, pos)
            if pos != []:
                pos = pos[index]
                self.Click( pos[0] + x, pos[1] + y)
                return True
            else:
                time.sleep(1)
        
        return False
    
    def GetSize(self):
        
        output = subprocess.check_output(
            f"adb -s {self.uid} shell wm size", shell=True)
        
        output = str(output).split(" ")[2][:-5]
        x, y = output.split("x")
        
        return int(x), int(y)
    
    def Close(self,  package):
        subprocess.check_call(
            f"adb -s {self.uid} shell am force-stop {package}", shell=True)
    
    def AirplaneMode(self ):
        subprocess.check_call(
            f"adb -s {self.uid} shell am start -a android.settings.AIRPLANE_MODE_SETTINGS", shell=True)
        time.sleep(1)
        self.TapXml( xpath='//node[@resource-id="com.android.settings:id/switch_widget"]', time_wait=5, x=40, y=20)
        time.sleep(4)
        self.TapXml( xpath='//node[@resource-id="com.android.settings:id/switch_widget"]', time_wait=5, x=40, y=20)
        time.sleep(3)
