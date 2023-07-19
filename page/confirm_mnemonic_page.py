"""确认助记词页面模型"""
import allure
from .base_page import BasePage

class ConfirmMnemonicPage(BasePage):
    # locator
    # 确认自动补全助记词button（测试环境）
    confirm_auto_complete_mnemonic_button = ("xpath","//button[text()=' 确定 ']")
    # 取消自动补全助记词button（测试环境）
    cancel_auto_complete_mnemonic_button = ("xpath","//button[text()=' 取消 ']")
    # 确认完成button
    confirm_finish_button = ("xpath","//button/bn-loading-wrapper/div[contains(text(),'完成')]")

    # action
    @allure.step("点击确认自动补全助记词按钮")
    def click_confirm_auto_complete_mnemonic_button(self):
        """点击自动补全助记词按钮"""
        self.click(self.confirm_auto_complete_mnemonic_button)

    @allure.step("点击取消自动补全助记词按钮")
    def click_cancel_auto_complete_mnemonic_button(self):
        """点击取消自动补全助记词按钮"""
        self.click(self.cancel_auto_complete_mnemonic_button)

    @allure.step("点击确认助记词完成按钮")
    def click_confirm_mnemonic_finish_button(self):
        """点击确认助记词完成按钮"""
        self.click(self.confirm_finish_button)