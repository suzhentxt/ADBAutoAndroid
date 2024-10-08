from AdbController import *
import uiautomator2 as u2

class Tiktok(ADB):
    def __init__(self, uid) -> None:
        super().__init__(uid)
        self.uid = uid
        self.driver = u2.connect(self.uid)
    
    def open(self):
        # print(self.driver.app_list_running())
        self.driver.app_start(package_name="com.ss.android.ugc.trill")

    def login(self):
        self.do_click_xpath(by_locator='//android.view.ViewGroup[@resource-id="com.ss.android.ugc.trill:id/i9f"]/android.widget.ImageView[1]', timeout=10000)
        
    def do_click_xpath(self, by_locator, timeout):
        try:
            self.driver.xpath(by_locator).click(timeout)
            return True
        except:
            return False
    
    def do_sendkeys_class_EditText(self, timeout, content):
        for _ in range(timeout):
            try:
                self.driver(className='android.widget.EditText').click(timeout=3)
                
                self.driver.send_keys(text=content, clear=False)
                return True
            except:
                time.sleep(1)
                
        return False
        
    def do_sendkeys_xpath(self, by_locator, timeout, content):
        for _ in range(timeout):
            try:
                for t in content:
                    self.driver.xpath(xpath=by_locator).set_text(text=t)
                return True
            except:
                time.sleep(1)
                
        return False

test = Tiktok(uid="emulator-5554")
test.open()
