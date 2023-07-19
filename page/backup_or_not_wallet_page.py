"""是否备份助记词页面模型"""
import allure
from .base_page import BasePage

class BackupOrNotWalletPage(BasePage):
    # locator
    # 立即备份助记词button
    backup_mnemonic_button = ("xpath","//button[text()='立即备份助记词']")
    # 跳过备份div
    skip_backup_mnemonic_div = ("xpath","//div[text()='跳过备份']")
    # 是否备份弹窗放弃备份button
    backup_abort_button = ("xpath","//common-card//button[text()=' 放弃备份 ']")
    # 是否备份弹窗取消button
    cancel_button = ("xpath","//common-card//button[text()=' 取消 ']")

    # action
    @allure.step("点击立即备份助记词")
    def click_backup_mnemonic_button(self):
        """点击立即备份助记词"""
        self.click(self.backup_mnemonic_button)

    @allure.step("点击跳过备份")
    def click_skip_backup_mnemonic_button(self):
        """点击跳过备份"""
        self.click(self.skip_backup_mnemonic_div)

    @allure.step("点击跳过备份弹窗放弃备份按钮")
    def click_backup_abort_button(self):
        """点击跳过备份弹窗放弃备份按钮"""
        self.click(self.backup_abort_button)

    @allure.step("点击跳过备份弹窗取消按钮")
    def click_backup_abort_cancel_button(self):
        """点击跳过备份弹窗取消按钮"""
        self.click(self.cancel_button)