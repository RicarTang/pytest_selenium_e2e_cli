import pytest
from page.login_page import LoginPage

login_page = LoginPage()

class TestCase:
    """测试用例类"""
    def test_create_wallet(self):
        """创建钱包"""
        pass
    
    @pytest.mark.demo
    def test_demo(self):
        login_page.driver.get("http://127.0.0.1:6939/")
        login_page.click_create_wallet_button()
