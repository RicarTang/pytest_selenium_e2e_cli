"""创建钱包页页面模型"""
import allure
from .base_page import BasePage

class CreateWalletPage(BasePage):
    # locator
    # 选择助记词语言button
    choose_mnemonic_language_button = ("xpath","//button/div[contains((text()),'English')]")
    # 选择助记词数量button
    choose_mnemonic_number_button = ("xpath","//button/div[contains((text()),'12 个字')]")
    # 用户协议checkbox
    user_agreement_checkbox = ("xpath","//input[@type='checkbox'and@id='agree']")
    # 用户协议
    user_agreement = ("xpath","//span[text()='用户协议']")
    # 创建钱包button
    create_wallet_submit = ("xpath","//button[@type='submit']")

    # acton    
    @allure.step("点击选择助记词语言")
    def click_choose_mnemonic_language(self):
        """点击选择助记词语言"""
        self.click(self.choose_mnemonic_language_button)

    @allure.step("点击选择助记词数量")
    def click_choose_mnemonic_number(self):
        """点击选择助记词数量"""
        self.click(self.choose_mnemonic_number_button)

    @allure.step("点击勾选用户协议")
    def click_user_agreement_checkbox(self):
        """点击勾选用户协议"""
        self.click(self.user_agreement_checkbox)

    @allure.step("点击查看用户协议")
    def click_view_user_agreement(self):
        """点击查看用户协议"""
        self.click(self.user_agreement)
    
    @allure.step("点击创建钱包按钮")
    def click_create_wallet_submit_button(self):
        """点击创建钱包按钮"""
        self.click(self.create_wallet_submit)
