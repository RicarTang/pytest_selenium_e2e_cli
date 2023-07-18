"""是否备份助记词页面模型"""
import allure
from .base_page import BasePage

class BackupOrNotWalletPage(BasePage):
    # locator
    # 立即备份助记词button
    backup_mnemonic_button = ("xpath","//button[text()='立即备份助记词']")
    # 跳过备份div
    skip_backup_mnemonic_div = ("xpath","//div[text()='跳过备份']")

    # action
    @allure.step("点击立即备份助记词")
    def click_backup_mnemonic_button(self):
        """点击立即备份助记词"""
        self.click(self.backup_mnemonic_button)

    @allure.step("点击跳过备份")
    def click_skip_backup_mnemonic_button(self):
        """点击跳过备份"""
        self.click(self.skip_backup_mnemonic_div)