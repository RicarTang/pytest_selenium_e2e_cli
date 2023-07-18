"""对selenium api二次封装"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import config as config


class Common:
    """公共类"""
    @property
    def driver(self):
        """driver"""
        # 使用webdriver_manager自动下载安装驱动，省去手动下载
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def locator(self,ele:tuple):
        """显示等待元素定位

        Args:
            ele (tuple): 定位器

        Returns:
            _type_: webdriver
        """
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*ele))

    
    def input(self, ele, value):
        """输入"""
        dr = self.locator(ele)
        dr.send_keys(value)

    def click(self, ele):
        """点击元素"""
        dr = self.locator(ele)
        print(type(dr))
        dr.click()

    def text(self, ele):
        """提取文字"""
        dr = self.locator(ele)
        return dr.text

    
    def save_screenshot(self):
        """屏幕捕获"""
        img = os.path.join(config.ROOT_PATH, 'screenshot', 'error', f"{time.strftime('%Y-%m-%d %H-%M-%S')}.png")
        # 保存图片到本地
        self.driver.save_screenshot(img) 
        