from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def install_driver():
    """
    下载浏览器驱动,
    使用webdriver_manager自动下载安装驱动，省去手动下载
    """
    try:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    except ValueError:
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    return driver
