"""备份助记词页面模型"""
import allure
from .base_page import BasePage

class BackupMnemonicPage(BasePage):
    # locator
    # 复制助记词button
    copy_mnemonic_button = ("xpath","//button[text()='复制助记词']")
    # 确认已备份button
    confirm_backedup_button = ("xpath","//button[text()='确认已备份']")

    # action
    @allure.step("点击复制助记词")
    def click_copy_mnemonic_button(self):
        """点击复制助记词"""
        self.click(self.copy_mnemonic_button)

    @allure.step("点击确认已备份按钮")
    def click_confirm_backedup_button(self):
        """点击确认已备份按钮"""
        self.click(self.confirm_backedup_button)