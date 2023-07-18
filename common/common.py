"""对selenium api二次封装"""
import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import config as config


# class Singleton(type):
#     """元类，单例模式"""
#     _instance_lock = threading.Lock()

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def __call__(cls, *args, **kwargs):
#         with cls._instance_lock:
#             if not hasattr(cls, "_instance"):
#                 cls._instance = super().__call__(*args, **kwargs)
#         return cls._instance


class Common:
    """公共类"""

    # 使用webdriver_manager自动下载安装驱动，省去手动下载
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def locator(self, ele: tuple) -> WebElement:
        """显示等待元素定位

        Args:
            ele (tuple): 定位器

        Returns:
            _type_: WebElement
        """
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*ele))

    def input(self, ele: tuple, value: str | int | float):
        """输入内容

        Args:
            ele (tuple): 定位器
            value (str | int | float): 输入值
        """
        webele = self.locator(ele)
        webele.send_keys(value)

    def click(self, ele:tuple):
        """点击元素"""
        webele = self.locator(ele)
        webele.click()

    def text(self, ele:tuple):
        """提取文字"""
        webele = self.locator(ele)
        return webele.text
    
    def get_attribute(self,ele:tuple,attribute:str):
        """获取元素属性值"""
        webele = self.locator(ele)
        return webele.get_attribute(attribute)

    def save_screenshot(self):
        """屏幕捕获"""
        img = os.path.join(
            config.ROOT_PATH,
            "screenshot",
            "error",
            f"{time.strftime('%Y-%m-%d %H-%M-%S')}.png",
        )
        # 保存图片到本地
        self.driver.save_screenshot(img)
