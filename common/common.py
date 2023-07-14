"""对selenium api二次封装"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import config



class Common:
    """公共类"""
    @property
    def driver(self):
        """driver"""
        # 使用webdriver_manager自动下载安装驱动，省去手动下载
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def locator(self,ele):
        """显示等待元素定位"""
        return WebDriverWait(self.dr, 10, 1).until(lambda x: x.find_element(*ele))

    
    def input(self, ele, value):
        """输入"""
        ele = self.locator(ele)
        ele.send_keys(value)

    def click(self, ele):
        """点击"""
        ele = self.locator(ele)
        ele.click()

    def text(self, ele):
        """提取文字"""
        ele = self.locator(ele)
        return ele.text

    
    def save_screenshot(self):
        """屏幕捕获"""
        img = os.path.join(config.ROOT_PATH,'screenshot','error',f"{time.strftime('%Y-%m-%d %H-%M-%S')}.png")
        # 保存图片到本地
        self.driver.save_screenshot(img) 
        