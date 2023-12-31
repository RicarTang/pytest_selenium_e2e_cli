"""登录页页面模型"""
import allure
from common.common import Common

class LoginPage(Common):
    # locator
    # 创建钱包按钮
    create_wallet_button = ("xpath","//button[text()='创建钱包']")
    # 恢复钱包按钮
    restore_wallet_button = ("xpath","//button[text()='恢复钱包']")

    # action
    @allure.step("点击创建钱包按钮")
    def click_create_wallet_button(self):
        """点击创建钱包按钮"""
        self.click(self.create_wallet_button)

    @allure.step("点击恢复钱包按钮")
    def click_restore_wallet_button(self):
        """点击恢复钱包按钮"""
        self.click(self.restore_wallet_button)