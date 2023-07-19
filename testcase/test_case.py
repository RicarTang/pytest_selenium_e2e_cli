# import pytest
# from page.login_page import LoginPage
# from page.create_wallet_page import CreateWalletPage


# class TestCase(LoginPage, CreateWalletPage):
#     """测试用例类"""


#     def teardown_class(self):
#         """后置操作"""
#         self.driver.quit()

#     def test_create_wallet(self):
#         """创建钱包"""
#         pass

#     @pytest.mark.skip
#     def test_demo(self):
#         self.driver.get("http://127.0.0.1:6939/")
#         self.click_create_wallet_button()
#         self.input_wallet_name("haojiahuo")
