"""放置页面公共元素"""
import allure
from common.common import Common

class BasePage(Common):
    # locator
    # 返回按钮
    go_back_button = ("xpath","//button[@mode='icon']")
    # 钱包名称input
    wallet_name_input = ("xpath","//input[@placeholder='输入1~12个字符']")
    # 钱包密码input
    wallet_pwd_input = ("xpath","//input[@placeholder='密码至少8个字符']")
    # 确认密码input
    wallet_confirm_pwd_input = ("xpath","//input[@placeholder='确认密码']")
    # 密码提示input
    wallet_pwd_hint_input = ("xpath","//input[@placeholder='输入密码提示信息']")

    # acton
    @allure.step("点击创建钱包返回按钮")
    def click_go_back(self):
        """点击返回按钮"""
        self.click(self.go_back_button)

    @allure.step("输入钱包名称")
    def input_wallet_name(self,wallet_name:str):
        """输入钱包名称"""
        self.input(self.wallet_name_input,wallet_name)

    @allure.step("输入钱包密码")
    def input_wallet_pwd(self,wallet_pwd:str|int):
        """输入钱包密码"""
        self.input(self.wallet_pwd_input,wallet_pwd)
    
    @allure.step("输入钱包确认密码")
    def input_wallet_confirm_pwd(self,wallet_pwd:str|int):
        """输入确认钱包密码"""
        self.input(self.wallet_confirm_pwd_input,wallet_pwd)

    @allure.step("输入钱包密码提示")
    def input_wallet_pwd_hint(self,wallet_pwd_hint:str):
        """输入钱包密码提示"""
        self.input(self.wallet_pwd_hint_input,wallet_pwd_hint)