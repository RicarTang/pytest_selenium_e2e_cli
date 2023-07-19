"""对selenium api二次封装"""
import os
import time
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import config
from utils.driver_manager import install_driver


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
    """
    公共类,
    对selenium的一些封装
    """
    driver = install_driver()

    def get(self,url_path:str):
        """封装driver.get()

        Args:
            url_path (str): 前端路由
        """
        self.driver.get(url=config.TEST_URL+url_path)

    def locator(self, ele: tuple) -> WebElement:
        """显示等待元素定位

        Args:
            ele (tuple): 定位器

        Returns:
            WebElement: web元素对象
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
        """点击元素

        Args:
            ele (tuple): WebElement
        """
        webele = self.locator(ele)
        webele.click()

    def text(self, ele:tuple):
        """获取文字

        Args:
            ele (tuple): WebElement
        """
        webele = self.locator(ele)
        return webele.text
    
    def get_attribute(self,ele:tuple,attribute:str) -> str:
        """获取元素属性值

        Args:
            ele (tuple): WebElement
            attribute (str): 元素属性名称

        Returns:
            str: attribute属性值
        """
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
