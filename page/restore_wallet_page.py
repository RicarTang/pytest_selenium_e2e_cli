"""恢复钱包页页面模型"""
import allure
from .base_page import BasePage

class RestoreWalletPage(BasePage):
    # locator
    
    # 助记词textarea
    mnemonic_textarea = ("xpath","//textarea[@type='text']")
    # 用户协议checkbox
    user_agreement_checkbox = ("xpath","//input[@type='checkbox'and@id='agree']")
    # 用户协议
    user_agreement = ("xpath","//span[text()='用户协议']")
    # 恢复钱包button
    restore_wallet_submit = ("xpath","//button[@type='submit']")

    # action
    @allure.step("输入助记词")
    def input_wallet_mnemonic(self,mnemonic:str):
        """输入助记词"""
        self.input(self.mnemonic_textarea,mnemonic)
    
    @allure.step("点击勾选用户协议")
    def click_user_agreement_checkbox(self):
        """点击勾选用户协议"""
        self.click(self.user_agreement_checkbox)

    @allure.step("点击查看用户协议")
    def click_view_user_agreement(self):
        """点击查看用户协议"""
        self.click(self.user_agreement)
    
    @allure.step("点击恢复钱包按钮")
    def click_restore_wallet_submit_button(self):
        """点击创建钱包按钮"""
        self.click(self.restore_wallet_submit)
